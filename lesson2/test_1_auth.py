'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Авторизация
1. Авторизация используя корректные данные (standard_user, secret_sauce)
2. Авторизация используя некорректные данные (user, user)
'''

from data import *
from locators import *


# case 1.1
def test_auth_positive(browser, login):
    assert browser.current_url == INVENTORY_URL


# case 1.2
def test_auth_negative(browser):
    browser.get(MAIN_PAGE_URL)
    browser.find_element(*USERNAME_FIELD).send_keys('user')
    browser.find_element(*PASSWORD_FIELD).send_keys('user')
    browser.find_element(*LOGIN_BUTTON).click()
    assert browser.find_element(*ERROR_MSG).text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == MAIN_PAGE_URL, 'Browser go to another URL'
