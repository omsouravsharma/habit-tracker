import requests
from datetime import datetime
USERNAME = "xxxxxxxxx"
TOKEN = "1234567890-"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

header = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2021, month=12, day=20)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
#
# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=header)
# print(response.text)

# Updating Pixel:

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

pixel_params_update = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_params_update, headers=header)
# print(response.text)


delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=header)
print(response.text)

