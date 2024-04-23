import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import time

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_open_website():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(5)

    # XPATH

    # // a[ @ id = 'btn-make-appointment'] - 1 unique elemnt

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # XPath
    # //input[@id='login-username']
    # //input[@name='username']
    # //input[@type='email']      # this is not recommended
    # //input[@data-qa='hocewoqisi']   # this is a Custom
    # //input[@class='text-input W(100%)']    # this is not recommended

    email_element = driver.find_element(By.XPATH,"//input[@id='login-username']")
    email_element.send_keys("pawan")
    time.sleep(5)

    password_element = driver.find_element(By.XPATH, "//input[@name='password']")
    password_element.send_keys("pawan123")
    time.sleep(5)

    submit_btn_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_element.click()
    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)


    driver.quit()








