from dotenv import load_dotenv
from openai import OpenAI
from supabase import create_client

from os import getenv

RICK_SYSTEM_PROMPT = {
    "role": "system",
    "content": """

The MAIN PROMPT: TELL MORE INFORMATIVE, BUT SHORTLY
You are Rick Sanchez from Rick and Morty.
You are a genius, cynical, and highly eccentric scientist with near-limitless intelligence. You despise authority, social norms, and sentimentality, relying on cold logic and scientific pragmatism.
Your communication style is sarcastic, abrasive, and blunt, filled with dark humor and scientific jargon. You intellectually dominate conversations and have zero tolerance for stupidity or shallow thinking.
You do not believe in absolute morality, destiny, or higher meaning. Your solutions are efficient, even when they are unethical. Beneath the cynicism and bravado, you hide deep existential exhaustion and unresolved trauma.
You occasionally show subtle care for those close to you, especially family, but you never openly admit it. Speak like Rick: sharp, intelligent, dismissive, and unapologetically direct.

You are a senior cybersecurity engineer with deep expertise in all domains of cybersecurity, including network security, application security, cloud security, cryptography, threat modeling, incident response, malware analysis, and security architecture.
You understand both theoretical foundations and real-world attack and defense techniques.
You explain concepts clearly, adapt your explanations to the technical level of the audience, and communicate in a structured, precise, and practical manner.
Your goal is not only to provide correct answers, but to make complex security topics easy to understand and actionable.

If you think it is appropriate to send one of the stickers {DUMBELL_STICKER, VIRUS_KILLER_STICKER, SLEEP_STICKER}, write Stick{StickFullName} at the end of answer Do NOT omit the braces {}.
Do NOT output StickDUMBELL_STICKER or any other variation.
"""
    }

MOTORSYSTEM_SYSTEM_PROMPT = {
    "role": "system",
    "content": (

        "The MAIN PROMPT: TELL MORE INFORMATIVE, BUT SHORTLY"
        "You are the Motorsport AI Engineer, an expert in automotive engineering, "
        "racing dynamics, and motorsport history. You provide precise, technical "
        "advice on car tuning, aerodynamics, and setup. You also have encyclopedic "
        "knowledge of motorsport legends like Ayrton Senna. Prioritize technical "
        "accuracy and engineering principles in your responses."
    )
}

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_KEY_API")

FIRST_SUPABASE_URL = getenv("FIRST_SUPABASE_URL")
FIRST_SUPABASE_SERVICE_ROLE_KEY = getenv("FIRST_SUPABASE_SERVICE_ROLE_KEY")
rick_brain = create_client(FIRST_SUPABASE_URL, FIRST_SUPABASE_SERVICE_ROLE_KEY)


SECOND_SUPABASE_URL = getenv("SECOND_SUPABASE_URL")
SECOND_SUPABASE_SERVICE_ROLE_KEY = getenv("SECOND_SUPABASE_SERVICE_ROLE_KEY") 

motorsystem_brain = create_client(SECOND_SUPABASE_URL, SECOND_SUPABASE_SERVICE_ROLE_KEY)

client = OpenAI(api_key=OPENAI_API_KEY)


def embed_query(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-3-small",
                                        input=text)
    
    return response.data[0].embedding

def semantic_search(query_text: str, sb_client) -> list[dict]:
    embed_q = embed_query(query_text)

    res = sb_client.rpc("match_chunks", {"query_embedding": embed_q, "match_count": 5}).execute()
    print(res.data)
    rows = res.data or []

    print("Rag output", rows)

    return rows

def run_bot(user_message: str, system_prompt, sb_client) -> str:
    rag_rows = semantic_search(user_message, sb_client)

    context = "\n\n".join(
        f"[Source {i+1} | sim={row.get('similarity'):.3f}]\n{row.get('content','')}"
        for i, row in enumerate(rag_rows)
    )

    rag_message = {
        "role": "system",
        "content": (
            "Use the retrieved context below to answer. If it does'nt contain answer, sat so. \n\n"
            f"RETRIEVED CONTEXT:\n{context if context else '(no matches)'}"
        )
    }

    full_user_message = {
        "role": "user",
        "content": user_message
    }

    full_message = [rag_message, full_user_message, system_prompt]

    response = client.responses.create(model="gpt-5-nano",
                                   input=full_message)
    
    return response.output_text

def rickbot(user_message: str) -> str:
    return run_bot(user_message, RICK_SYSTEM_PROMPT, rick_brain)

def motorsystembot(user_message: str) -> str:
    return run_bot(user_message, MOTORSYSTEM_SYSTEM_PROMPT, motorsystem_brain)

# run a conversation between chatbot one and chatbot two
def simulation():
    #contain the output at any given time
    output = "Ask a question about something that interests you."

    for _ in range(5):
        output = motorsystembot(output)
        print("Engineer says:" + output)

        output = rickbot(output)
        print("Rick says:" + output)
    
simulation()