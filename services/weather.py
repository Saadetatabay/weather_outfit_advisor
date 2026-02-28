from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key= os.getenv("API_KEY_WEATHER")


url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city:str):
    params={"q":city,"appid":api_key,"units":"metric"}
    response = requests.get(url,params)
    response.raise_for_status()
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return(temp,description)


