from decouple import config
import requests

COMPANY_NAME = "AMAZON"
NEWS_API = config("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
    "language": "en"
}


def get_news():
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"][:3]
    return articles

get_news()
