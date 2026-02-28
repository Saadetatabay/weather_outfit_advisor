from dotenv import load_dotenv
import os
from google import generativeai

load_dotenv()
api_key = os.getenv("API_KEY_GEMINI")
model = generativeai.GenerativeModel("gemini-2.5-flash")

def get_outfit_advice(temp,description):
    generativeai.configure(api_key=api_key)
    prompt="Given the temperature in Celsius and the weather description, provide outfit advice. Temperature: {}°C, Weather: {}".format(temp,description)
    response=model.generate_content(prompt)
    return response.text

