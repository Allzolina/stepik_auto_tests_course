from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Hello")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Selenium")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test")
    input_file = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'l2_s7.txt')
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
