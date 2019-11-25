from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

user = "tien.dao@terralogic.com"
pwd = "1Ylcotlmi"
driver = webdriver.Firefox()
driver.get("http://intranet.terralogic.com")
#assert "Facebook" in driver.title
elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem = driver.find_element_by_id("signin")
elem.submit()
#elem.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 5)

driver.close()

