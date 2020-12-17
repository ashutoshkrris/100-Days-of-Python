# from decouple import config
# import smtplib

# my_email = config('EMAIL')
# my_password = config('PASSWORD')
# to_email = config("RECEIVER")

# with smtplib.SMTP('smtp.gmail.com') as server:
#     server.starttls()
#     server.login(user=my_email, password=my_password)
#     server.sendmail(
#         from_addr=my_email, 
#         to_addrs=to_email, 
#         msg="Subject:Hello\n\nHiiiiiiiiiiiii"
#     )

import datetime

# print(datetime.datetime.now())
now = datetime.datetime.now()
print(now.time())