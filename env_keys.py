from dotenv import load_dotenv
from os import getenv

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
TG_BOT_API = getenv("TG_BOT_API")
SUPABASE_URL = getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = getenv("SUPABASE_SERVICE_ROLE_KEY")