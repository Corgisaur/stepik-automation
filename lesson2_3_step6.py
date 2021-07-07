from selenium import webdriver
import time
import math
import os


try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    newWindow = browser.window_handles[1]
    browser.switch_to.window(newWindow)



    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    findX = browser.find_element_by_id("input_value")
    x = findX.text
    y = calc(x)

    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
