import requests


def get_coordinates(city: str):
    params = {"name": city, "count": 1, "language": "ru"}

    response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params=params)

    return response.json()["results"][0] if len(response.json()["results"]) > 0 else None


def get_weather(latitude:float, longitude: float):
    params = {"latitude": latitude, "longitude": longitude,
                "current": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"]}
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)

    return response.json().get("current")


city = input("Введите город: ")

coordinates = get_coordinates(city)
weather = get_weather(coordinates["latitude"], coordinates["longitude"])

print(f"Город: {coordinates["name"]}")
print(f"Температура: {weather.get('temperature_2m')}")
print(f"Скорость ветра: {weather.get('wind_speed_10m')}")
print(f"Влажность: {weather.get('relative_humidity_2m')} %")