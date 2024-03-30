'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Авторизация
1. Авторизация используя корректные данные (standard_user, secret_sauce)
2. Авторизация используя некорректные данные (user, user)
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

def user_auth():
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


# case 1.1
def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    user_auth()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'
    assert browser.title == 'Swag Labs', 'Wrong browser title'


# case 1.2
def test_auth_negative():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    error_text = browser.find_element('xpath', '//h3').text
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == 'https://www.saucedemo.com/v1/', 'Browser go to another URL'

