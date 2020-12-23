from twilio.rest import Client
from decouple import config

TWILIO_SID = config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = config("FROM_NUMBER")
TWILIO_VERIFIED_NUMBER = config("TO_NUMBER")


class NotificationManager:

    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
