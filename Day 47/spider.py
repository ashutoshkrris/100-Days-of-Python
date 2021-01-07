import requests
import lxml
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}


def get_latest_price(url):
    product_details = {}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, features='lxml')
    try:
        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text()
        price_without_currency = price.split("₹")[1]
        product_details['price'] = float(price_without_currency)
        product_details['title'] = title
        return product_details
    except:
        return "Couldn't extract data"

