'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Карточка товара
1. Успешный переход к карточке товара после клика на картинку товара
2. Успешный переход к карточке товара после клика на название товара
'''

from data import *
from locators import *


# case 3.1
def test_click_on_item_img(browser, login):
    # pick item description:
    item_desc1 = browser.find_element(*ITEM_DESC).text

    # pick item image and click:
    browser.find_element(*ITEM_IMG).click()

    # check if url changed and we can get the same item:
    item_card_desc1 = browser.find_element(*ITEM_CARD_DESC).text
    assert browser.current_url != INVENTORY_URL, 'Wrong URL'
    assert item_desc1 == item_card_desc1, 'Different item description'


# case 3.2
def test_click_on_item_title(browser, login):
    # pick item description:
    item_desc1 = browser.find_element(*ITEM_DESC_1).text

    # pick item title and click:
    browser.find_element(*ITEM_TITLE).click()

    # check if url changed and we can get the same item:
    item_card_desc1 = browser.find_element(*ITEM_CARD_DESC_1).text
    assert browser.current_url != MAIN_PAGE_URL, 'Wrong URL'
    assert item_desc1 == item_card_desc1, 'Different item description'
