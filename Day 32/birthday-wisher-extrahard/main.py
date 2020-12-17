##################### Extra Hard Starting Project ######################

from datetime import datetime
import smtplib
import pandas as pd
import random
from decouple import config


my_email = config('EMAIL')
my_password = config('PASSWORD')
to_email = config("RECEIVER")

today_date = datetime.now().day
today_month = datetime.now().month
today_tuple = (today_month,today_date)

df = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file_data:
        contents = file_data.read()
        new_contents = contents.replace("[NAME]", birthday_dict[today_tuple]["name"])

    with smtplib.SMTP('smtp.gmail.com') as server:
        server.starttls()
        server.login(user=my_email, password=my_password)
        server.sendmail(
            from_addr=my_email, 
            to_addrs=to_email, 
            msg=f"Subject:Happy Birthday\n\n{new_contents}"
        )

