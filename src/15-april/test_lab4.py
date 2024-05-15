

from selenium import webdriver
import time

# def test_open_vwologin():

#     driver = webdriver.Chrome()
#     driver.get("https://bing.com/chat")
#     time.sleep(5)  # Python Int.- wait for the 5 seconds, not the webdriver.
#     driver.get("https://google.com")
#     print(driver.title)


def test_open_vwologin():

    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(5)
    driver.get("https://www.youtube.com")
    time.sleep(5)

    driver.back()    # back browser
    time.sleep(5)

    driver.forward()  # forward browser
    time.sleep(5)

    driver.refresh()  # refresh browser
    time.sleep(5)

