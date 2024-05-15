from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


# def test_dropdown_select():
#     driver = webdriver.Edge()
#     driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#     driver.maximize_window()
#     time.sleep(5)
#
#     dropdown_menu = driver.find_element(By.ID,"dropdown-class-example")
#     # when make x path in inspact select is must important in coding then use this rule
#     select = Select(dropdown_menu)
#     select.select_by_index(2)   # method 1 get dropdown value
#     time.sleep(3)
#
#     select.select_by_value("option1")   # method 2 get dropdown value
#     time.sleep(3)
#
#     select.select_by_visible_text("Option3")   # method 3 get dropdown value
#     time.sleep(3)

#---------------------------------------------------------------------------------------------

# other method we can find the dropdown value

def test_dropdown_select():
    driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']")
    dropdown_element.click()
    time.sleep(3)

    dropdown_element2 = driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']//option["
                                                     "@value='option2']")

    dropdown_element2.click()
    time.sleep(3)








