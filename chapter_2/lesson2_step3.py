from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return x + y

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text

    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    answer = str(calc(int(x), int(y)))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
