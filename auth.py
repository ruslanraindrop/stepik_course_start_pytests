import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSendAnswers:
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize('number_page', ["236895", "236896", "236897", "236898",
                                             "236899", "236903", "236904", "236905"])
    def test_answers(self, browser, number_page):
        link = f"https://stepik.org/lesson/{number_page}/step/1"
        browser.get(link)

        login_button = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR,
                                        ".ember-view.navbar__auth.navbar__auth_login"))
        )
        login_button.click()

        login_input = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.ID, "id_login_email"))
        )
        login_input.send_keys("YOUR_LOGIN")

        password_input = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.ID, "id_login_password"))
        )
        password_input.send_keys("YOUR_PASSWORD")

        submit_button = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn.button_with-loader"))
        )
        submit_button.click()

        login_form = WebDriverWait(browser, 3).until(
            ec.invisibility_of_element_located((By.CSS_SELECTOR, ".box"))
        )
        print(login_form)

        text_input = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']"))
        )
        answer = math.log(int(time.time()))
        text_input.send_keys(answer)

        answer_submit = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        answer_submit.click()
        result = WebDriverWait(browser, 15).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

        assert result == "Correct!", f"Ошибка: выводится текст {result}"
