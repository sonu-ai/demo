
# from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/home/admin7/Downloads/seleniumBrowser/chromedriver")
driver.get("https://testerwork.com/")
driver.maximize_window()
driver.find_element(By.XPATH,'//* [@class="buttons sf-menu"]//child::li[2]/a[@href="https://testers.testerwork.com/tester-account/sign-up" ]').click()
time.sleep(3)
ele=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/label/span[1]//*[@id="app"]/div/div[2]/div[1]/div[2]/di1]/label/span[1]').is_selected()
time.sleep(3)
if(ele==is_selected()):
    print("Login Succesful")
    time.sleep(3)
else:
    ele.click()
    time.sleep(5)
driver.close()