"""
Необходимо написать несколько автотестов для сайта <https://the-internet.herokuapp.com/ опираясь на полученные знания
и поиск в интернете новой информации.

Ссылки на упражнения:

1. <https://the-internet.herokuapp.com/add_remove_elements/> (Необходимо создать и удалить элемент)
2. <https://the-internet.herokuapp.com/basic_auth> (Необходимо пройти базовую авторизацию)
3. <https://the-internet.herokuapp.com/broken_images> (Необходимо найти сломанные изображения)
4. <https://the-internet.herokuapp.com/checkboxes> (Практика с чек боксами)

Так же важно помнить что мы должны получать информацию об веб-элементах и сравнивать ее с ожидаемым результатом.

Например: текст, цвет, расположение, отображение, выбор чекбокса и так далее.
Ссылка на страницу с документацией: <https://www.selenium.dev/documentation/webdriver/elements/information/>
"""
import time

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# DATA
CONGRATS_MSG = 'Congratulations! You must have the proper credentials.'

# LOCATORS
ADD_ELEMENT_BTN = ('xpath', '//button[text()="Add Element"]')
DELETE_BTN = ('xpath', '//button[text()="Delete"]')
CONGRATS_BOX = ('xpath', '//p')

# URLS
URL_1 = 'https://the-internet.herokuapp.com/add_remove_elements/'
URL_2 = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'  # Login credentials are in the URL
URL_3 = 'https://the-internet.herokuapp.com/broken_images'
URL_4 = 'https://the-internet.herokuapp.com/checkboxes'


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

    yield browser
    browser.quit()


@pytest.fixture()
def exp_wait(browser):
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    return wait


# 1. Необходимо создать и удалить элемент
def test_add_delete_element(browser, exp_wait):
    browser.get(URL_1)

    exp_wait.until(EC.visibility_of_element_located(ADD_ELEMENT_BTN)).click()

    assert exp_wait.until(EC.visibility_of_element_located(DELETE_BTN)), "The DELETE button is not displaying"

    exp_wait.until(EC.visibility_of_element_located(DELETE_BTN)).click()

    assert exp_wait.until(EC.invisibility_of_element_located(DELETE_BTN)), "The DELETE button is still displaying"


# 2. Необходимо пройти базовую авторизацию
def test_basic_auth(browser, exp_wait):
    browser.get(URL_2)

    assert exp_wait.until(EC.visibility_of_element_located(CONGRATS_BOX)).text == CONGRATS_MSG


# 3. Необходимо найти сломанные изображения
def test_broken_images(browser, exp_wait):
    browser.get(URL_3)

    assert browser.find_element('xpath', '//h3').text == "Broken Images", "Wrong page is displaying"

    images = browser.find_elements('xpath', '//div/img')
    broken_images = []

    print("")
    for image in images:
        src = image.get_attribute("src")
        if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f"Broken image found")

    print("List of broken images:")
    if broken_images:
        for broken_image in broken_images:
            print(broken_image)
    else:
        print("No broken images were found")


# 4. Практика с чек боксами
def test_checkbox(browser, exp_wait):
    browser.get(URL_4)

    assert browser.find_element('xpath', '//h3').text == "Checkboxes", "Wrong page is displaying"

    checkboxes = browser.find_elements('xpath', '//input[@type="checkbox"]')

    for checkbox in checkboxes:
        if checkbox.is_selected():
            print("The checkbook is selected")
        else:
            checkbox.click()
