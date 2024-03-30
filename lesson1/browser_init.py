from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import time

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
success_url = 'https://www.saucedemo.com/checkout-complete.html'
cart_url = 'https://www.saucedemo.com/cart.html'
about_url = 'https://saucelabs.com/'