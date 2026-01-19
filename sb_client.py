from supabase import create_client

from env_keys import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

sb = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
