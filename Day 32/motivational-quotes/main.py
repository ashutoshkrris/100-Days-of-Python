from datetime import datetime
import smtplib
import random
from decouple import config

my_email = config('EMAIL')
my_password = config('PASSWORD')
to_email = config("RECEIVER")

def email_sender():
    with open("quotes.txt") as file_data:
        quotes = file_data.readlines()
    today_quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as server:
        server.starttls()
        server.login(user=my_email, password=my_password)
        server.sendmail(
            from_addr=my_email, 
            to_addrs=to_email, 
            msg=f"Subject:Today's Motivational Quote\n\n{today_quote}"
        )

weekday = datetime.now().weekday()
if weekday==0:
    email_sender()
else:
    print("Today is not Monday.")


