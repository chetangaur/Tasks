from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get(url="http://www.newtours.demoaut.com/")
user_ele=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input")
print(user_ele.is_displayed())
print(user_ele.is_enabled())
pas_ele=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input")
print(pas_ele.is_displayed())
print(pas_ele.is_enabled())
user_ele.send_keys("mercury")
pas_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

