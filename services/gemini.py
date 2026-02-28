from dotenv import load_dotenv
import os
from google import genai


def get_outfit_advice(temp,description):
    client = genai.Client(api_key=os.getenv("API_KEY_GEMINI"))
    prompt="Given the temperature in Celsius and the weather description, provide outfit advice. Temperature: {}°C, Weather: {}".format(temp,description)
    response=client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
    return response.text

