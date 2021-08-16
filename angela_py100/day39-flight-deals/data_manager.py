import requests
import json
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def getdata():
        sheety_get = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfFlightDeals/prices"
        response = requests.get(url=sheety_get)
        print("sheety get:", response.text)
        return response.json()

    def update(element):
        row_id = element["id"]
        print("row_id: ", row_id)

        sheety_put = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfFlightDeals/prices/"
        url = sheety_put + str(row_id)
        body = {
            "price": {
                "city": element["city"],
                "iataCode": element["iataCode"],
                "id": element["id"],
                "lowestPrice": element["lowestPrice"]
            }
        }
        body = json.dumps(body)
        # print("body: ", body)
        headers = {"Content-Type": "application/json"}

        response = requests.put(url=url, data=body, headers=headers)
        # print("sheety update:", response.json() )
        return response.json()
