# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from datetime import datetime
import os
# APP_ID = os.environ["NT_APP_ID"]
# API_KEY = os.environ["NT_API_KEY"]

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = raw_input("Tell me which exercises you did: ")

post_body = {
 "query": exercise_text,
 "gender": "male",
 "weight_kg": 70.5,
 "height_cm": 169.0,
 "age": 44
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "x-remote-user-id": 0
}

response = requests.post(url=endpoint, json=post_body, headers=headers)
resjson = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in resjson["exercises"]:
    sheety_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_post = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfMyWorkouts/workouts"
    response = requests.post(url=sheety_post, json=sheety_body)

# print("response 0:", str(resjson["exercises"][0]) )
# print("\n")
# print("response 1:", str(resjson["exercises"][1]) + "\n\n")
# "duration_min"
# "nf_calories"
# sheety_body = {
#     "workout": {
#         "date": "20210815",
#         "time": "1533",
#         "exercise": "walk",
#         "duration": "30",
#         "calories": "130.25"
#     }
# }
#
# sheety_get = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfMyWorkouts/workouts"
# response = requests.get(url=sheety_get)
# print("\n")
# print("sheety get:", response.json())
#
# response = requests.post(url=sheety_post, json=sheety_body)
# print("\n")
# print("sheety post:", response)

sheety_get = "https://api.sheety.co/0ba339e71ea2eb52f839c03ad23f9e5b/copyOfMyWorkouts/workouts"
response = requests.get(url=sheety_get)
print("sheety get:", response.json())

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
