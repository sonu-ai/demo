import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="/home/admin7/Downloads/seleniumBrowser/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="demo"]//parent::div[1]').click()
time.sleep(5)
driver.switch_to.accept()
# driver.switch_to_alert().dismiss()