from fastapi import FastAPI
from app.weather import get_weather_data

app = FastAPI()

@app.get("/get_weather_of_the_day")
async def get_weather_of_the_day(lat: float, lon: float):
    weather_data = await get_weather_data(lat, lon)
    return weather_data
