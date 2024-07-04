from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_weather_of_the_day():
    response = client.get("/get_weather_of_the_day?lat=35.6895&lon=139.6917")
    assert response.status_code == 200
    assert "source1" in response.json()
    assert "source2" in response.json()
    assert "source3" in response.json()
