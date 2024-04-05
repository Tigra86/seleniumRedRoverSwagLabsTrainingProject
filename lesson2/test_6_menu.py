'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Бургер меню
1. Выход из системы
2. Проверка работоспособности кнопки "About" в меню
3. Проверка работоспособности кнопки "Reset App State"
'''

from data import *
from locators import *


# case 6.1
def test_positive_logout(browser, login):
    # find and click burger menu:
    browser.find_element(*BURGER_BTN).click()

    # find and click 'logout' button:
    browser.find_element(*LOGOUT_BTN).click()

    # check if we are on login page:
    assert browser.current_url == MAIN_PAGE_URL


# case 6.2
def test_positive_about_btn(browser, login):
    # find and click burger menu:
    browser.find_element(*BURGER_BTN).click()

    # find and click 'about' button:
    browser.find_element(*ABOUT_BTN).click()

    # check expected url and title:
    curr_title = browser.title
    exp_title = 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing'
    assert browser.current_url == ABOUT_URL and curr_title == exp_title, 'Wrong page url or title'


# case 6.3
def test_reset_app_state_positive(browser, login):
    # add two items to cart:
    browser.find_element(*ADD_TO_CART_BTN_1).click()
    browser.find_element(*ADD_BOLT_T_SHIRT_ITEM).click()

    # find and click burger menu:
    browser.find_element(*BURGER_BTN).click()

    # find and click 'reset app state' button:
    browser.find_element(*RESET_BTN).click()

    # check if cart is empty:
    cart_tag3 = browser.find_element('css selector', '#shopping_cart_container>a:empty')
    assert bool(cart_tag3) == True, 'Shopping cart is not empty'
