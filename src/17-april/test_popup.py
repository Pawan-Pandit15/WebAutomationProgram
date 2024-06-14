# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# def test_open_website():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
#     input_box = driver.find_element(By.NAME, "enter-name")
#     input_box.send_keys("Pawan")
#
#     alert_button = driver.find_element(By.XPATH, "//input[@class='btn-style']")
#     alert_button.click()
#
#     # driver.implicitly_wait(5)  #( Implicit wait )
#     WebDriverWait(driver,10).until(EC.alert_is_present()) # explicit wait
#
#     popup = driver.switch_to.alert
#     print(popup.text)
#
#     assert "Pawan" in popup.text
#
#     popup.accept()
#
#     confirm_btn = driver.find_element(By.XPATH, "//input[@id='confirmbtn']")
#     confirm_btn.click()
#
#     print(popup.text)
#
#     assert popup.text == "Hello , Are you sure you want to confirm?"
#
#     popup.dismiss()










