import httpx

async def fetch_weather(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

async def get_weather_data(lat: float, lon: float):
    sources = [
        f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={lat},{lon}",
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=YOUR_API_KEY",
        f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key=YOUR_API_KEY"
    ]

    weather_responses = await httpx.gather(*(fetch_weather(url) for url in sources))

    combined_weather_data = {
        "source1": weather_responses[0],
        "source2": weather_responses[1],
        "source3": weather_responses[2],
    }

    return combined_weather_data
