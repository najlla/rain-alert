import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a4e56c21f4640c10325cb10695db95b3"
account_sid = "ACe618ac1601343b5ad994795ce121be75"
auth_token = "8ef4c9118f7c9b2f29c29170c5b06e8c"

parameters = {
    "lat": 34.555347,
    "lon": 69.207489,
    "appid": api_key,
    "exclude": "current,minutely,daily",

}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
# Slice notation in python
slice_weather = weather_data["hourly"][:12]

will_rain = False

for hour_data in slice_weather:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18597109613",
        to="+93706625153"
        )
    print(message.status)
