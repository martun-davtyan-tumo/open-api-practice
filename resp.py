from dotenv import load_dotenv
from openai import OpenAI
from env_keys import OPENAI_API_KEY

from sb_client import sb
from ready_messages import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


load_dotenv()

def get_response_text(user_input: str) -> str:
    rag_rows = semantic_search(user_input)

    context = "\n\n".join(
        f"[Source {i+1} | sim={row.get('similarity'):.3f}]\n{row.get('content','')}"
        for i, row in enumerate(rag_rows)
    )

    sys_prompt_message = {
        "role": "system",
        "content": SYSTEM_PROMPT
    }

    rag_message = {
        "role": "system",
        "content": (
            "Use the retrieved context below to answer. If it does'nt contain answer, sat so. \n\n"
            f"RETRIEVED CONTEXT:\n{context if context else '(no matches)'}"
        )
    }

    full_user_message = {
        "role": "user",
        "content": user_input
    }

    full_message = [rag_message, full_user_message, sys_prompt_message]

    response = client.responses.create(model="gpt-5-nano",
                                   input=full_message)
    
    return response.output_text

def embed_query(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-3-small",
                                        input=text)
    
    return response.data[0].embedding

def semantic_search(query_text: str) -> list[dict]:
    embed_q = embed_query(query_text)

    res = sb.rpc("match_chunks", {"query_embedding": embed_q, "match_count": 5}).execute()
    print(res.data)
    rows = res.data or []

    print("Rag output", rows)

    return rows

pr_ref = "frvpzrhpasustlbmvmoe"
pr_name = "swift-api"
pr_secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZydnB6cmhwYXN1c3RsYm12bW9lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjgzOTEwMDEsImV4cCI6MjA4Mzk2NzAwMX0.mmUO-jBMApHLLESUcy2HzKSSXBAlktFPBupgjDzJxw8"

print(f'''curl -X POST "https://{pr_ref}.functions.supabase.co/{pr_name}" \\
       -H "Content-Type: application/json" \\
      -H "Authorization: Bearer {pr_secret_key}" \\
      
      ''')