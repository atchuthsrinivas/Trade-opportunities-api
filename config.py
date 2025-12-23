from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY = os.getenv("API_KEY")
RATE_LIMIT = os.getenv("RATE_LIMIT", "5/minute")
