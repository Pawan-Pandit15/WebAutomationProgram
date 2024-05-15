
# Selenium 4


from selenium import webdriver

import time
import allure

#----------------------------------------------------------------
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

#--------------------------------------------------------------------

# def test_open_vwologin():
#     driver = webdriver.Chrome() # POST request | Create the Session
#     driver.get("https://app.vwo.com") # GET Request to URL param
#     print(driver.title)  # here print browser Title
#     driver.maximize_window()  # here maximize the browser
#     time.sleep(5)   # here open browser 5 second
#     print(driver.page_source)  # here print all HTML code in this program
#     print(driver.session_id)   # here create unique session id
#     driver.close()   # this is close only one tab
#     driver.quit()  # this is close all browser tab ( Whole browser )
#     assert driver.title == "Login - VWO"

#------------------------------------------------------------------------





