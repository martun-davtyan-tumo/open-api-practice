from dotenv import load_dotenv
from openai import OpenAI
from env_keys import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

load_dotenv()

def get_response_text(user_input: str) -> str:
    response = client.responses.create(model="gpt-5-nano",
                                   input=user_input)
    
    return response.output_text