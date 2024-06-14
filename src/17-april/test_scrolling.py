from selenium import webdriver
import time


def test_open_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 3200)")  # Vertical Page Scroll Down Side
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0)")  # Scroll upper side

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll Bottom of the page
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(3)

    pixel = 1000  # scroll step by step
    for step in range(0, 3):
        driver.execute_script("window.scrollTo(0, " + str(pixel) + ")")
        pixel = 1000 + pixel
        time.sleep(1)
