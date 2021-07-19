from selenium import webdriver
import time
import math
import unittest


class TestReg(unittest.TestCase):
        def test_link_reg1(self):
            options = webdriver.ChromeOptions()
            browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
            browser.get("http://suninjuly.github.io/registration1.html")

            input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
            input3.send_keys("Smolensk@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "FAILED")

        def test_link_reg2(self):
            options = webdriver.ChromeOptions()
            browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)  # webdriver path
            browser.get("http://suninjuly.github.io/registration2.html")

            input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
            input3.send_keys("Smolensk@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "FAILED")


if __name__ == "__main__":
    unittest.main()
