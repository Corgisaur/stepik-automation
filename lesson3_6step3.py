import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('user_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, user_id):
    link = f"https://stepik.org/lesson/{user_id}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    txtfield = browser.find_element_by_tag_name('textarea')
    txtfield.send_keys(str(answer))
    button_submit = browser.find_element_by_css_selector("button.submit-submission")
    button_submit.click()
    answer_field = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    browser.implicitly_wait(5)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    if answer_field != "Correct!":
        print(answer_field)


