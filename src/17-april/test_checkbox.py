from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_multiple_checkbox():
    driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)
    # check_box_element = driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']")
    # check_box_element.click()   # this is click only one check box
    # time.sleep(5)



    # multi_checkbox_element = driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
    # print(multi_checkbox_element)
    # print(len(multi_checkbox_element))
    # for check_box in multi_checkbox_element:
    #     check_box.click()
    #
    # time.sleep(5)
    #
    # driver.refresh()
    #
    # multi_checkbox_element1 = driver.find_elements(By.XPATH, "(//input[starts-with(@name,'checkBoxOption')])["
    #                                                          "position()<3]")

    # for check_box1 in multi_checkbox_element1:
    #     check_box1.click()
    #
    # time.sleep(5)

    multi_checkbox_element = driver.find_elements(By.XPATH, "//input[starts-with(@name,'checkBoxOption')]")

    for check_box in multi_checkbox_element:
        if multi_checkbox_element.index(check_box)+1 < 3:
            check_box.click()

    time.sleep(5)









