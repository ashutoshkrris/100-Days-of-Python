from bs4 import BeautifulSoup
import requests

article_texts = []
article_links = []
article_scores = []

response = requests.get("https://news.ycombinator.com/")
hn_webpage = response.text

soup = BeautifulSoup(hn_webpage, "html.parser")
article_tag = soup.find_all(name="a", class_="storylink")
for item in article_tag:
    article_tag_text = item.get_text()
    article_texts.append(article_tag_text)
    article_tag_link = item.get("href")
    article_links.append(article_tag_link)

article_tag_upvote = soup.find_all(name="span", class_="score")
for data in article_tag_upvote:
    points = data.text.split(" ")[0]
    article_scores.append(int(points))

# print(article_texts)
# print(article_links)
# print(article_scores)

max_upvotes_index = article_scores.index(max(article_scores))
print(article_texts[max_upvotes_index], article_links[max_upvotes_index], max(article_scores))
