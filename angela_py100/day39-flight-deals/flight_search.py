import os
import requests

tequila_key = os.environ["TEQUILA_API_KEY"]
from datetime import datetime, timedelta

class FlightSearch:
    def getIATA(self, element):
        headers = {
            "apikey": tequila_key
        }
        city = element["city"]
        kiwi_url = f"https://tequila-api.kiwi.com/locations/query?term={city}&locale=en-US&location_types=airport&limit=10&active_only=true"
        city_code = requests.get(url=kiwi_url, headers=headers)
        city_code = city_code.json()["locations"][0]["city"]["code"]
#        print("city_code: ", city_code)
        return city_code

        #This class is responsible for talking to the Flight Search API.

    def searchFlight(self, element):
        origin_city_code = "LON"
        destination_city_code = element["iataCode"]
        from_time = datetime.now() + timedelta(days=1)
        to_time = datetime.now() + timedelta(days=(6*30))

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        search_url = "https://tequila-api.kiwi.com/v2/search"
        headers = {
            "apikey": tequila_key
        }
        flight_result = requests.get(url=search_url, headers=headers, params=query).json()
        print("flight_result: ", flight_result)
        return flight_result
