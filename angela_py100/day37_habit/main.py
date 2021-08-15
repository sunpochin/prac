import requests

#USERNAME = "pionhack"
USERNAME = "patricksoon"
#USERNAME = "patrick"
GRAPH_ID = "graph1"

TOKEN = "abcdefgh"
#TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text )

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print("end_point: ", graph_endpoint)
graph_config = {
    "id": GRAPH_ID,
    "name": "cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
print("headers: ", headers)
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("graph:", response.json())

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

from datetime import datetime
today = datetime.today().strftime('%Y%m%d')
#today = datetime.today().strftime('20210801')
print("post_pixel: ", post_endpoint)
print("today: ", today)
pixel_config = {
    "date": today,
    "quantity": input("How many kilometers did you run today?")
}

response = requests.post(url=post_endpoint, json=pixel_config, headers=headers)
print("pixel response:", response.text)

# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# put_config = {
#     "quantity": "9.9",
# }
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print("put response:", response.json())
