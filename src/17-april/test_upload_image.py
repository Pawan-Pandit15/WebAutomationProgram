import time

from selenium import webdriver
from selenium.webdriver.common.by import By




def test_open_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(5)
    upload_btn = driver.find_element(By.XPATH,"//input[@name='file']")
    # file upload xpath input tag compulsory
    time.sleep(5)
    upload_btn.send_keys("C:\\Users\\pawan\\Desktop\\Pawan.jpg")
    time.sleep(5)
    upload_b = driver.find_element(By.XPATH,"//input[@id='file-submit']")
    upload_b.click()
    time.sleep(10)



