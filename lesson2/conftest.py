from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from data import *
from locators import *


@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.page_load_strategy = "eager"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-cache")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options, service=service)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login(browser):
    browser.get(MAIN_PAGE_URL)
    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(*LOGIN_BUTTON).click()
