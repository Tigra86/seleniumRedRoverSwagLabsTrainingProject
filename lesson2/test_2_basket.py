'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Корзина
1. Добавление товара в корзину через каталог
2. Удаление товара из корзины через корзину
3. Добавление товара в корзину из карточки товара
4. Удаление товара из корзины через карточку товара
'''

from data import *
from locators import *


# case 2.1
def test_add_to_cart(browser, login_form):
    # add item to cart:
    browser.find_element(*ADD_TO_CART_BTN_1).click()

    # go to cart:
    browser.find_element(*CART_ICON).click()

    assert browser.find_element(*ITEM_1).text == browser.find_element(*PICKED_ITEM_1).text, 'Different item picked'

    # remove item from cart:
    browser.find_element(*RMV_FROM_CART_BTN_1).click()


# case 2.2
def test_remove_from_cart(browser, login_form):
    # pick items and add to cart:
    browser.find_element(*ADD_BOLT_T_SHIRT_ITEM).click()
    browser.find_element(*ADD_RED_T_SHIRT_ITEM).click()

    # go to cart:
    browser.find_element(*CART_ICON).click()

    # remove items from cart:
    browser.find_element(*RMV_BOLT_T_SHIRT_ITEM).click()
    browser.find_element(*RMV_RED_T_SHIRT_ITEM).click()

    # check if cart quantity tag is missing on page:
    assert CART_TAG_ICON not in browser.page_source, 'Items are not removed from cart'


# case 2.3
def test_add_item_from_item_card(browser, login_form):

    # find item link and click it:
    browser.find_element(*ITEM_TITLE_4).click()

    # check if item title is the same item title:
    assert browser.find_element(*ITEM_TITLE_3).text == browser.find_element(*CARD_ITEM_TITLE_3).text, 'Wrong item'

    # add to cart:
    browser.find_element(*ADD_TO_CART_BTN).click()

    # go to cart:
    browser.find_element(*CART_ICON).click()

    # check if item title is the same item title and url is cart url:
    assert browser.current_url == CART_URL, 'Wrong url'

    # remove item from cart:
    browser.find_element('xpath', '//button[@id="remove-sauce-labs-backpack"]').click()


# case 2.4
def test_remove_item_from_item_card(browser, login_form):
    # add item to cart:
    browser.find_element(*ADD_TO_CART_BTN_1).click()

    # go to item card:
    browser.find_element(*ITEM_1).click()
    assert browser.find_element(*ITEM_1).text == 'Sauce Labs Backpack', 'Wrong item title'

    # click remove button:
    browser.find_element(*RMV_FROM_CART_BTN).click()

    # check the button changed:
    assert browser.find_element(*ADD_TO_CART_BTN).text == 'Add to cart', 'Button didn\'t change'