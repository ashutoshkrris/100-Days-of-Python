# Download the helper library from https://www.twilio.com/docs/python/install
from decouple import config
from twilio.rest import Client
from news import get_news

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
STOCK = "AMZN"
data = get_news()


def send_sms(arrow):
    body = [
        f"\n{STOCK}: {arrow} \nHeadline: {article['title']} \nBrief: {article['description']}" for article in data]
    for mes in body:
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=mes,
                            from_='',
                            to=''
                        )
        print(message.body)
        print(message.status)
