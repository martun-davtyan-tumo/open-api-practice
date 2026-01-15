from dotenv import load_dotenv
from openai import OpenAI
from env_keys import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

load_dotenv()

def get_response_text(user_input: str) -> str:
    response = client.responses.create(model="gpt-5-nano",
                                   input=user_input)
    
    return response.output_text


# pr_ref = "frvpzrhpasustlbmvmoe"
# pr_name = "swift-api"
# pr_secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZydnB6cmhwYXN1c3RsYm12bW9lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjgzOTEwMDEsImV4cCI6MjA4Mzk2NzAwMX0.mmUO-jBMApHLLESUcy2HzKSSXBAlktFPBupgjDzJxw8"

# print(f'''curl -X POST "https://{pr_ref}.functions.supabase.co/{pr_name}" \\
#        -H "Content-Type: application/json" \\
#       -H "Authorization: Bearer {pr_secret_key}" \\
      
#       ''')