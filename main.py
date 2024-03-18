from dotenv import load_dotenv

load_dotenv()

import os


genius_client_id = os.getenv("GENIUS_CLIENT_ID")
genius_client_secret = os.getenv("GENIUS_CLIENT_SECRET")

print(genius_client_id, genius_client_secret)
