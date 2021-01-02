from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# all_a_tags = soup.find_all(name="a")
# for tag in all_a_tags:
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)