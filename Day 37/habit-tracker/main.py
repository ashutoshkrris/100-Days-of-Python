import requests
from decouple import config
from datetime import datetime

USERNAME = config("PIXELA_USERNAME")
TOKEN = config("TOKEN")
GRAPH_ID = "graph1"
DATE = datetime.now().strftime("%Y%m%d")

USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create User

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=USER_ENDPOINT, json=user_params)
# print(response.json())

# Create Graph
# graph_params = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora"
# }

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.json())


# Create pixel

# pixel_params = {
#     "date":DATE,
#     "quantity":"9.46"
# }

# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
# print(response.json())

# # Update a pixel

# pixel_params = {
#     "quantity":"9.86"
# }

# response = requests.put(url=f"{PIXEL_ENDPOINT}/{DATE}", json=pixel_params, headers=headers)
# print(response.json())

# Delete a pixel

response = requests.delete(url=f"{PIXEL_ENDPOINT}/{DATE}", headers=headers)
print(response.json())
