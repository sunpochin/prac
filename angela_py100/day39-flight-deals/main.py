# . ~/pythonvar.sh  # first

import os
import requests
from twilio.rest import Client
import pprint
from data_manager import DataManager
from flight_search import FlightSearch


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

twilio_num = os.environ['TWILIO_NUM']
target_num = os.environ['TARGET_NUM']
sms_msg = 'hi pachinko'

# message = client.messages.create(
#     body=sms_msg,
#     from_=twilio_num,
#     to=target_num
# )

# print(message.sid)

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.


# sheety_get = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfFlightDeals/prices"
# response = requests.get(url=sheety_get)
# pprint("sheety get:", response.json())



# sheet_data = DataManager.getdata()["prices"]

pp = pprint.PrettyPrinter(width=38, compact=True)
# pp.pprint("\n")
# pp.pprint(prices)
sear = FlightSearch()
for element in sheet_data:
    print("ele: ", element)
    iataCode = sear.getIATA(element)
    element["iataCode"] = iataCode
#    ret = DataManager.update(element)

    result = sear.searchFlight(element)



pp.pprint(sheet_data)

