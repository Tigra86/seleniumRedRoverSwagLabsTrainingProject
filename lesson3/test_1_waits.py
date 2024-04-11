"""
Домашнее задание
Суть данного домашнего задания - тренировка использования ожиданий в Selenium, повторение пройденных тем перед
написанием полноценного тестового фреймворка.

Для практики я попросил ChatGPT написать небольшой сайт с формой регистрации. Ссылка на сайт:
https://victoretc.github.io/selenium_waits/

Вам необходимо автоматизировать данный тест кейс используя ранее пройденные темы, включая ожидания.

Название Теста: Проверка функционала регистрации на сайте

Предусловия: Браузер открыт, интернет-соединение стабильно.

Шаги:
- Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
- Проверить заголовок: Убедиться, что текст в теге h1 на странице соответствует "Практика с ожиданиями в Selenium".
- Дождаться появления кнопки "Начать тестирование"
- Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
- Начать тестирование: Кликнуть по кнопке "Начать тестирование".
- Ввод логина: Ввести "login" в поле для логина.
- Ввод пароля: Ввести "password" в поле для пароля.
- Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
- Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
- Проверка загрузки: Удостовериться, что появился индикатор загрузки.
- Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
- Ожидаемый результат: Пользователь успешно проходит процесс регистрации, видит индикатор загрузки и получает сообщение
об успешной регистрации.

Критерии успешности: Сообщение "Вы успешно зарегистрированы" отображается на экране.

Необходимо написать 3 автотеста для данной страницы:
1. С использованием Explicit waits и Expected Conditions
2. С использованием Implicit waits
3. С использованием time.sleep()
"""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# DATA
PAGE_NAME_TEXT = 'Практика с ожиданиями в Selenium'
LOGIN_TEXT = 'login'
PWD_TEXT = 'password'
SUCCESS_MSG = 'Вы успешно зарегистрированы!'

# LOCATORS
PAGE_NAME = ('xpath', '//h1')
START_TEST_BTN = ('xpath', '//button[@id="startTest"]')
LOGIN_FLD = ('xpath', '//input[@id="login"]')
PWD_FLD = ('xpath', '//input[@id="password"]')
CHECKBOX = ('xpath', '//input[@id="agree"]')
REG_BTN = ('xpath', '//button[@id="register"]')
LOADER = ('xpath', '//div[@id="loader"]')
SUCCESS_BOX = ('xpath', '//p[@id="successMessage"]')

# URLS
WAITS_URL = 'https://victoretc.github.io/selenium_waits/'


@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.page_load_strategy = "eager"
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-cache")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options, service=service)

    browser.get(WAITS_URL)

    yield browser
    browser.quit()


# 1. С использованием Explicit waits и Expected Conditions
def test_explicit_wait(browser):
    wait = WebDriverWait(browser, 30, poll_frequency=1)

    assert wait.until(EC.visibility_of_element_located(PAGE_NAME)).text == PAGE_NAME_TEXT, ("The page name is not "
                                                                                            "correct")

    wait.until(EC.visibility_of_element_located(START_TEST_BTN)).click()
    wait.until(EC.visibility_of_element_located(LOGIN_FLD)).send_keys(LOGIN_TEXT)
    wait.until(EC.visibility_of_element_located(PWD_FLD)).send_keys(PWD_TEXT)
    wait.until(EC.visibility_of_element_located(CHECKBOX)).click()
    wait.until(EC.visibility_of_element_located(REG_BTN)).click()

    assert wait.until(EC.visibility_of_element_located(LOADER)), "The loader is not displaying"
    assert wait.until(EC.visibility_of_element_located(SUCCESS_BOX)).text == SUCCESS_MSG, ("The success message is not "
                                                                                           "displaying")


# 2. С использованием Implicit waits
def test_implicit_wait(browser):
    browser.implicitly_wait(15)
    assert browser.find_element(*PAGE_NAME).text == PAGE_NAME_TEXT, "The page name is not correct"

    browser.find_element(*START_TEST_BTN).click()
    browser.find_element(*LOGIN_FLD).send_keys(LOGIN_TEXT)
    browser.find_element(*PWD_FLD).send_keys(PWD_TEXT)
    browser.find_element(*CHECKBOX).click()
    browser.find_element(*REG_BTN).click()

    assert browser.find_element(*LOADER), "The loader is not displaying"
    time.sleep(3)  # test falls without time.sleep here
    assert browser.find_element(*SUCCESS_BOX).text == SUCCESS_MSG, "The success message is not displaying"


# 3. С использованием time.sleep()

def test_time_sleep_wait(browser):
    assert browser.find_element(*PAGE_NAME).text == PAGE_NAME_TEXT, "The page name is not correct"
    time.sleep(7)

    browser.find_element(*START_TEST_BTN).click()
    browser.find_element(*LOGIN_FLD).send_keys(LOGIN_TEXT)
    browser.find_element(*PWD_FLD).send_keys(PWD_TEXT)
    browser.find_element(*CHECKBOX).click()
    browser.find_element(*REG_BTN).click()
    time.sleep(7)

    assert browser.find_element(*LOADER), "The loader is not displaying"
    time.sleep(3)
    assert browser.find_element(*SUCCESS_BOX).text == SUCCESS_MSG, "The success message is not displaying"
