import pytest
import allure
from allure_commons.types import AttachmentType

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# actions = ActionChains(driver)      # use multi line
# actions.move_to_element(menu)
# actions.click(hidden_submenu)
# actions.perform()


# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()     # use one line

def test_open_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    name_element = driver.find_element(By.LINK_TEXT, "Login")
    name_element.click()

    actions = ActionChains(driver)
    # actions.move_to_element(driver.find_element(By.XPATH,"//div[text()='More']")).perform()
    # actions.move_to_element(driver.find_element(By.XPATH, "//div[text()='Notification Preferences']")).click().perform()
    # time.sleep(2)
    # assert driver.current_url == "https://www.flipkart.com/communication-preferences/push?t=all"
    #
    # driver.back()

    actions.move_to_element(driver.find_element(By.XPATH, "//div[text()='More']")).perform()
    actions.move_to_element(driver.find_element(By.XPATH, "//div[text()='24x7 Customer Care']")).click().perform()
    time.sleep(3)

    assert driver.current_url == "https://www.flipkart.com/helpcentre"

    flipkart_icon_click = driver.find_element(By.XPATH,"//img[@title='Flipkart']")
    flipkart_icon_click.click()

    search_input = driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']")
    search_input.click()

    #---------------------------------------------------------------------------------------------------------------

    #  Use Keyboard
    # method 1
    actions.key_down(Keys.DOWN).send_keys("Mobile").key_up(Keys.UP).perform()
    actions.send_keys(Keys.ENTER).perform()


    # method 2
    # actions.key_down(Keys.DOWN)
    # actions.send_keys("Phone")
    # actions.key_up(Keys.UP)
    # actions.perform()
    # actions.send_keys(Keys.ENTER)
    # actions.perform()

    time.sleep(5)

    # allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
