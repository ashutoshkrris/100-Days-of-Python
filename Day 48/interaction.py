from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()

# count = driver.find_element_by_link_text("6,224,073")
# count.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()