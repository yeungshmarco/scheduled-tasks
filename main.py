from venv import create

import requests
import os
from twilio.rest import Client

# api_key = "e34d2936925fe334e9cb49cc6e0304bc"
api_key = os.environ.get("WEATHER_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH")

parameters = {
    "lat": 22.396427,
    "lon": 114.109497,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(f"Status Code: {response.status_code}")

data = response.json()["list"]
for datapoint in data:
    weather_id = datapoint["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring an umbrella.",
            from_="whatsapp:+14155238886",
            to="whatsapp:+85246752419",
        )
        print(message.status)
        break

