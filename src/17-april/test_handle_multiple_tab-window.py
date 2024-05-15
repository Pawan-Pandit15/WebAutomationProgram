
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_website():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    new_window = driver.find_element(By.XPATH,"//button[@id='openwindow']")
    new_window.click()

    new_tab = driver.find_element(By.XPATH,"//a[@id='opentab']")
    new_tab.click()

    print(driver.window_handles)

    driver.switch_to.window(driver.window_handles[1])

    click_blog_element = driver.find_element(By.XPATH,"//ul[@class='navbar-nav ml-auto']//a[text()='Blog']")
    click_blog_element.click()

