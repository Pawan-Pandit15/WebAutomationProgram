
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(5)
    name_element = driver.find_element(By.LINK_TEXT, "Login")
    name_element.click()
    time.sleep(5)
    phone_number_element = driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']")
    phone_number_element.send_keys("9960374334")
    time.sleep(5)
    send_otp_element = driver.find_element(By.XPATH,"//button[@class='QqFHMw twnTnD _7Pd1Fp']")
    send_otp_element.click()
    time.sleep(5)
    print(driver.title)
    login="https://www.flipkart.com/account/login?ret=/"

    assert login == "https://www.flipkart.com/account/login?ret=/"




