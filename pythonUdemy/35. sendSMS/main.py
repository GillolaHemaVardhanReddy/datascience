import requests as req
from twilio.rest import Client

apikey = ""
url = "https://api.openweathermap.org/data/2.5/forecast"
ac_sid = ""
auth_token = ""


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