from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    frame_element = driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")
    driver.switch_to.frame(frame_element)
    # time.sleep(2)
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='consulting']")))

    job_support_element = driver.find_element(By.XPATH,"//a[@href='consulting']")
    job_support_element.click()

    driver.switch_to.default_content()

    type_name_display_example_element = driver.find_element(By.XPATH,"//input[@id='displayed-text']")
    type_name_display_example_element.send_keys("Pawan Pandit")
    time.sleep(2)


