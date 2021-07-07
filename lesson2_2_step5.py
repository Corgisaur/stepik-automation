from selenium import webdriver
import time
import math


try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    findX = browser.find_element_by_id("input_value")
    x = findX.text
    y = calc(x)
    txtField = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", txtField)
    txtField.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for ='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for = 'robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
