
# id -> name -> className -> tagName -> LinkText, PartialText -> css Selector -> Xpath

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_website():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(5)

    username_element = driver.find_element(By.NAME,"username")
    username_element.send_keys("Pawan")
    time.sleep(5)

    password_element = driver.find_element(By.NAME,"password")
    password_element.send_keys("Pawan123")
    time.sleep(5)

    btn_login_element = driver.find_element(By.ID,"js-login-btn")
    btn_login_element.click()
    time.sleep(5)

    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)
    time.sleep(5)

    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()

