import requests
from decouple import config

SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
TOKEN = config("SHEETY_TOKEN")


class DataManager:
    """ This class is responsible for talking to the Google Sheet. """

    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
