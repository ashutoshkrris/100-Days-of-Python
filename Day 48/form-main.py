from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("Ashutosh")

lname = driver.find_element_by_name("lName")
lname.send_keys("Krishna")

email = driver.find_element_by_name("email")
email.send_keys("ashutosh@gmail.com")

button = driver.find_element_by_css_selector("form button")
button.click()
