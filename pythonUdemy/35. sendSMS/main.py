import requests as req
from twilio.rest import Client

apikey = "1259e4550a8e1dcf27b38835ada745ac"
url = "https://api.openweathermap.org/data/2.5/forecast"
ac_sid = "ACa7de503a573aabe7d63c856b9a9a6a2c"
# use the damn tk in 2nd parameter = "e2025e98bb0f24803c33ffbbecd1132a"


parameters = {
    "lat" : 16.342050 ,
    "appid" : apikey ,
    "lon" : 77.908180 ,
    "cnt" : 4 ,
}
response = req.get(url, params=parameters)
response.raise_for_status()
data = response.json()
for item in data['list'] :
    if int(item['weather'][0]['id']) < 700 :
        client = Client(ac_sid, auth_token)
        message = client.messages.create(
                body="it's going to rain today, keep an umbrella aside you", 
                from_= "+17209247491",
                to= "+91 9390633050"
            )
        print(message.status)
        break