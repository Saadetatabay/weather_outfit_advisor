from dotenv import load_dotenv
import os
from google import generativeai

load_dotenv()
api_key = os.getenv("API_KEY_GEMINI")
generativeai.configure(api_key=api_key)
model = generativeai.GenerativeModel("gemini-1.5-flash-002")

