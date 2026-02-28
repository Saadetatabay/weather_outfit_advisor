from fastapi import FastAPI
from models import WeatherRequest,WeatherResponse
from services.gemini import get_outfit_advice
from services.weather import get_weather
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return f.read()


@app.post("/advice")
def root(request:WeatherRequest):
    cityname = request.city
    temp,desc=get_weather(cityname)
    text=get_outfit_advice(temp,desc)
    return WeatherResponse(city=cityname,temperature=temp,description=desc,outfit_advice=text)