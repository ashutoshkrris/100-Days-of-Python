from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for time in event_times:
#     print(time.text)
# for name in event_names:
#     print(name.text)

events = {}

for e in range(len(event_names)):
    events[e] = {
        "time": event_times[e].text,
        "title": event_names[e].text
    }

print(events)

driver.quit()
