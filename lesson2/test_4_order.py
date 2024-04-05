'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Оформление заказа
1. Оформление заказа используя корректные данные
'''

from data import *
from locators import *


# case 4.1
def test_positive_order(browser, login_form):
    # pick item and add it to cart:
    browser.find_element(*ADD_FLEECE_ITEM).click()

    # go to cart:
    browser.find_element(*CART_ICON).click()

    # go to checkout:
    browser.find_element(*CHECKOUT_BTN).click()

    # fill a form:
    browser.find_element(*F_NAME_FIELD).send_keys('Jane')
    browser.find_element(*L_NAME_FIELD).send_keys('Smith')
    browser.find_element(*ZIPCODE_FIELD).send_keys('123456')

    # click 'continue' button:
    browser.find_element(*CONTINUE_BTN).click()

    # click 'finish' button:
    browser.find_element(*FINISH_BTN).click()

    # check success message:
    success_msg = browser.find_element('xpath', '//h2[@data-test="complete-header"]').text

    assert browser.current_url == SUCCESS_URL and success_msg == 'Thank you for your order!', 'Wrong url'
