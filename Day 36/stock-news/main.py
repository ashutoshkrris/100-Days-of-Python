from decouple import config
import requests
from sms import send_sms

STOCK = "AMZN"
STOCK_API = config("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
json_data = response.json()["Time Series (Daily)"]

# Turing the response json data into list
data_list = [value for (key, value) in json_data.items()]

# Extracting yesterday's data
yesterday_data = data_list[0]
yesterday_closing = float(yesterday_data["4. close"])
# print(yesterday_closing)

# Extracting day before yesterday's data
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = float(day_before_yesterday_data["4. close"])
# print(day_before_yesterday_closing)

# Finding the positive difference
diff = (yesterday_closing-day_before_yesterday_closing)


up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Difference Percent
diff_percent = round((diff/yesterday_closing)*100)

# If percent is greater than 5%, get news
if abs(diff_percent) >= 0:
    send_sms(up_down)
