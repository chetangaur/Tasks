from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get(url="https://www.expedia.com/")

driver.find_element_by_xpath("//*[@id='package-origin-hp-package']").send_keys("Jaipur")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='package-destination-hp-package']").send_keys("Delhi")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='package-departing-hp-package']").send_keys("10/11/2019")

driver.findElement("").clear();
driver.find_element_by_xpath("//*[@id='package-returning-hp-package']").clear()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='package-returning-hp-package']").send_keys("10/16/2019")

#wait = WebDriverWait(driver,10)
#element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='search-button-hp-package']")))
#element.click()

time.sleep(5)

driver.quit()