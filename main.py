import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your api key"
account_sid = "Your twillo account id"
auth_token = "your twillo auth token"

# The below parameters are taken from the API parameters given already
weather_params = {
    "lat":31.230391,                 #17.914881,
    "lon":121.473701,                           #77.504608,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.cookies)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0])
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = False
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_="from no",
        to="to no"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="No need of an Umbrella =  ☔. No rain!!",
        from_="from no",
        to="to no"
    )
    print(message.status)
