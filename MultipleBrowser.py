from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get(url="http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(10)
driver.close() # to close the focused browser
driver.quit() # to close all web browsers