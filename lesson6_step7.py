from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
    browser.get(link)


    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("ответ")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла