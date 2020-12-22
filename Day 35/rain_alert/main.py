import requests
import json
from sms import send_sms
from decouple import config

api_key = config("api_key")
lon = 85
lat = 24.78
units = 'metric'

params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'exclude': "current,minutely,daily",
    'units': units
}

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/onecall", params=params)

data = response.json()
with open("weather.json", "w") as file:
    json.dump(data, file, indent=2)

will_rain = False

# print(data["hourly"][0]["weather"][0]["id"])
hourly_forecast = data["hourly"][:12]
# print(hourly_forecast)
for hour in hourly_forecast:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    send_sms()
