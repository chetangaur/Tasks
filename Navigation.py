from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get(url="https://www.google.com/search?q=hello&rlz=1C1CHBF_enIN813IN813&oq=hello&aqs=chrome..69i57j0l5.984j0j0&sourceid=chrome&ie=UTF-8")
print(driver.title)
time.sleep(5)
driver.get(url="https://www.google.com/search?q=Beliver+song&rlz=1C1CHBF_enIN813IN813&oq=Beliver+song&aqs=chrome..69i57j0l5.3992j1j0&sourceid=chrome&ie=UTF-8")
print(driver.title)
time.sleep(5)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.quit()