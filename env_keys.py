from dotenv import load_dotenv
from os import getenv

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
TG_BOT_API = getenv("TG_BOT_API")
