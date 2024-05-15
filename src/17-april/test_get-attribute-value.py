

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# here test flipkart offers sliders
def test_flipkart_attribute_value():
    driver = webdriver.Edge()
    driver.get("https://www.flipkart.com/")
    attribute_value = driver.find_element(By.XPATH,"//div[@data-clone='false']//a")
    print("Attribute Value :",attribute_value.get_attribute('href'))


    # find multiple flipkart banner attribute value

    attribute_value = driver.find_elements(By.XPATH, "//div[@data-clone='false']//a")
    print("Total Attribute Value :",len(attribute_value))

    for attribute in attribute_value:
        print(attribute.get_attribute("href"))




        




