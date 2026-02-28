from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city:str

class WeatherResponse(BaseModel):
    city:str
    temperature:float
    description:str
    outfit_advice:str

