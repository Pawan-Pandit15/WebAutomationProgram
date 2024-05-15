
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_open_website():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"username")))  # Explicit wait

    username_element = driver.find_element(By.NAME,"username")
    username_element.send_keys("Pawan")

    password_element = driver.find_element(By.NAME,"password")
    password_element.send_keys("Pawan123")

    btn_login_element = driver.find_element(By.ID,"js-login-btn")
    btn_login_element.click()

    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))  # explicit wait

    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()