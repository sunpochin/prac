import requests
from datetime import datetime
import time
MY_LAT = 23.6978 # Your latitude
MY_LONG = 120.9605 # Your longitude
# 23.6978° N, 120.9605° E


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    print("iss_latitude: ", iss_latitude)
    print("iss_longitude: ", iss_longitude)
    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # sunrise = (data["results"]["sunrise"])
    # sunset = (data["results"]["sunset"])

    time_now = datetime.now()
    now_hour = int(str(time_now).split(" ")[1].split(":")[0])
    print("now_hour: ", now_hour)
    print("sunrise: ", sunrise)
    print("sunset: ", sunset)
    if (now_hour >= (sunset + 8) and now_hour <= (sunrise + 8) ):
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if is_iss_overhead() and is_night():
        print("iss up!")
    else:
        print("no iss..")
    time.sleep(1)
