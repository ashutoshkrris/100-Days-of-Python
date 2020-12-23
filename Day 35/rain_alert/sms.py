# Download the helper library from https://www.twilio.com/docs/python/install
from decouple import config
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')


def send_sms():
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It'll 🌧 today. Be sure to bring an ☂.",
                        from_='',
                        to=''
                    )

    print(message.status)
