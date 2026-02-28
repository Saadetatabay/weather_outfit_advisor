from fastapi import FastAPI
from models import WeatherRequest,WeatherResponse
from services.gemini import get_outfit_advice
from services.weather import get_weather

app = FastAPI()

@app.post("/")
def root(request:WeatherRequest):
    cityname = request.city
    temp,desc=get_weather(cityname)
    text=get_outfit_advice(temp,desc)
    return WeatherResponse(city=cityname,temperature=temp,description=desc,outfit_advice=text)