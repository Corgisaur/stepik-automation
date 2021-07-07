from selenium import webdriver
import time
import math
import os


try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys('ivan')
    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys('petrov')
    email = browser.find_element_by_name("email")
    email.send_keys('test@test.tu')
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currentDir, 'file.txt')
    chooseFile = browser.find_element_by_id("file")
    chooseFile.send_keys(filePath)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
