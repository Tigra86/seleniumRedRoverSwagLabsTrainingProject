'''
Домашнее задание к первому уроку
Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:

Фильтр
1. Проверка работоспособности фильтра (A to Z)
2. Проверка работоспособности фильтра (Z to A)
3. Проверка работоспособности фильтра (low to high)
4. Проверка работоспособности фильтра (high to low)
'''

from locators import *


# case 5.1
def test_a_to_z_filter(browser, login):
    # sort items a-z before clicking on a-z filter:
    items_before1 = browser.find_elements(*CARD_ITEM_TITLE_3)
    before1 = []
    for item in items_before1:
        before1.append(item.text)

    before1.sort(reverse=False)
    print(f'\n{before1}')

    # click a-z filter:
    browser.find_element(*A_TO_Z_FILTER).click()

    # check if filter works properly:
    items_after1 = browser.find_elements(*CARD_ITEM_TITLE_3)
    after1 = []
    for item in items_after1:
        after1.append(item.text)
    print(f'\n{after1}')

    assert before1 == after1, 'Filter A to Z doesn\'t work properly'


# case 5.2
def test_z_to_a_filter(browser, login):
    # sort items z-a before clicking on a-z filter:
    items_before2 = browser.find_elements(*CARD_ITEM_TITLE_3)
    before2 = []
    for item in items_before2:
        before2.append(item.text)

    before2.sort(reverse=True)
    print(f'\n{before2}')

    # click z-a filter:
    browser.find_element(*Z_TO_A_FILTER).click()

    # check if filter works properly:
    items_after2 = browser.find_elements(*CARD_ITEM_TITLE_3)
    after2 = []
    for item in items_after2:
        after2.append(item.text)
    print(f'\n{after2}')

    assert before2 == after2, 'Filter Z to A doesn\'t work properly'


# case 5.3
def test_high_to_low_filter(browser, login):
    # sort items low-high before clicking on low-high filter:
    prices_before3 = browser.find_elements(*ITEM_PRICE_LIST)
    before3 = []
    for item in prices_before3:
        before3.append(float(item.text.lstrip('$')))

    before3.sort(reverse=False)
    print(f'\n{before3}')

    # click low-high filter:
    browser.find_element(*LOW_TO_HIGH_FILTER).click()

    # check if filter works properly:
    prices_after3 = browser.find_elements(*ITEM_PRICE_LIST)
    after3 = []
    for item in prices_after3:
        after3.append(float(item.text.lstrip('$')))
    print(f'\n{after3}')

    assert before3 == after3, 'Filter Low to High doesn\'t work properly'


# case 5.4
def test_low_to_high_filter(browser, login):
    # sort items low-high before clicking on low-high filter:
    prices_before4 = browser.find_elements(*ITEM_PRICE_LIST)
    before4 = []
    for item in prices_before4:
        before4.append(float(item.text.lstrip('$')))

    before4.sort(reverse=True)
    print(f'\n{before4}')

    # click low-high filter:
    browser.find_element(*HIGH_TO_LOW_FILTER).click()

    # check if filter works properly:
    prices_after4 = browser.find_elements(*ITEM_PRICE_LIST)
    after4 = []
    for item in prices_after4:
        after4.append(float(item.text.lstrip('$')))
    print(f'\n{after4}')

    assert before4 == after4, 'Filter Low to High doesn\'t work properly'