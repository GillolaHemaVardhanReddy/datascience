import requests
from datetime import datetime
from emailtest import sendmail

MY_LAT = 16.380297 # Your latitude
MY_LONG = 77.940845 # Your longitude
def isoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 :
        return True
    return False
#Your position is within +5 or -5 degrees of the ISS position.

def isnight():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now>= sunset or time_now <= sunrise:
        return True
    return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if isoverhead and isnight :
    sendmail(
        frm="gillolahemavardhanreddy@gmail.com", 
        to="balabittu1143@gmail.com", 
        subject="Look Up\n", 
        body = "Look above you you have an ISS station near you on the sky"
    )