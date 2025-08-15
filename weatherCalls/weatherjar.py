import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def getLocation():
    response = requests.get("http://ip-api.com/json/").json()
    if response['status'] == 'success':
        return {
            "city": response['city'],
            "region": response['regionName'],
            "country": response['country'],
            "lat": response['lat'],
            "lon": response['lon']
        }
    return None

def getWeather(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=imperial"
    )
    data = requests.get(url).json()
    if data.get("weather"):
        return {
            "description": data["weather"][0]["description"].capitalize(),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"]
        }
    return None

def getWeatherByZip(zip_code, country_code="US"):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"zip={zip_code},{country_code}&appid={OPENWEATHER_API_KEY}&units=imperial"
    )
    data = requests.get(url).json()
    if data.get("weather"):
        return {
            "description": data["weather"][0]["description"].capitalize(),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"]
        }
    return None


def showWeather(setZip):
    weather = getWeatherByZip(setZip)
    if not weather:
        return str("Could not get weather data.")

    return str(f"{weather['description']} {weather['temperature']}°F,"
          f"FL {weather['feels_like']}°F,Humidity: {weather['humidity']}%")

# FOR FUTURE FORMATTING USEAGE
#     print(f"Weather in {location['city']}, {location['region']} ({location['country']}):")
#     print(f"{weather['description']}, {weather['temperature']}°C "
#     f"(feels like {weather['feels_like']}°C), Humidity: {weather['humidity']}%")
