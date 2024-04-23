# ID - Unique ID
# name, Unique ClassName,
# TagName - get 1, list of elements via findElements
# Link/ partial - a anchor tags
# Css Selector - 20%
# XPath - 60%

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_website():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)

    # By. Link Text

        # Full Match or Exact match with the Text
        # rule 1 - first one, if there is not link text it will not able to find the element
        # a tag -> anchor tag

        # <a
        # id="btn-make-appointment"
        # href="./profile.php#login"
        # class="btn btn-dark btn-lg">
        # Make Appointment
        # </a>

    # btn_make_appointment = driver.find_element(By.LINK_TEXT,"Make Appointment")
    # btn_make_appointment.click()
    # time.sleep(5)


    # Partial Text

        # a anchor
        # partial match
        # PARTIAL_LINK_TEXT
        # Make Appointment
        # Appointment
        # Make
        # App
        # ment
        # Contains - keyword
        # Find the first unique element

    # btn_make_appointment = driver.find_element(By.PARTIAL_LINK_TEXT,"Make")
    # btn_make_appointment.click()
    # time.sleep(5)



    # Tag Name
    # Tag name find a anchor
    # go to page inspact click Ctrl+f type a and press enter navigate point and show how many number in that element
    # here element word put (s) that is elements because list of element there in page

    btn_make_appointment = driver.find_elements(By.TAG_NAME,"a")
    list_of_element = btn_make_appointment[5]
    list_of_element.click()
    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"


    driver.quit()






