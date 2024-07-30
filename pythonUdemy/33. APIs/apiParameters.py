import requests as req

api = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat":16.380297,
    "lng":77.940845,
    "formatted" : 0
}

response = req.get(api,params=parameters)
data = response.json()["results"]
sunraise = data["sunrise"]
sunset = data["sunset"]
print(sunset.split("T")[1].split(":")[0])