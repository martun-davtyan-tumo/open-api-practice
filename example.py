from dotenv import load_dotenv
from openai import OpenAI
# "whazzzzzzzzuuuuuup"
load_dotenv()

client = OpenAI()

user_input = input("Scribere promptum: ")

response = client.responses.create(model="gpt-5-nano",
                                   input=user_input)


print(response.output_text)