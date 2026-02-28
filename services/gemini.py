from dotenv import load_dotenv
import os
from google import generativeai

load_dotenv()
api_key = os.getenv("API_KEY_GEMINI")
generativeai.configure(api_key=api_key)
model = generativeai.GenerativeModel("gemini-1.5-flash-002")

def get_outfit_advice(temp,description):
    prompt="Given the temperature in Celsius and the weather description, provide outfit advice. Temperature: {}°C, Weather: {}".format(temp,description)
    response=model.generate_content(prompt)
    return response.text

