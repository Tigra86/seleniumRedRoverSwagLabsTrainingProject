# AUTH
USERNAME_FIELD = ('xpath', '//*[@id="user-name"]')
PASSWORD_FIELD = ('xpath', '//*[@id="password"]')
LOGIN_BUTTON = ('xpath', '//*[@id="login-button"]')
ERROR_MSG = ('xpath', '//*[@id="login_button_container"]//h3')

# CART
ITEM_1 = ('xpath', '//div[contains(text(), "Sauce Labs Backpack")]')
ADD_TO_CART_BTN_1 = ('css selector', 'button[data-test="add-to-cart-sauce-labs-backpack"]')
CART_ICON = ('css selector', 'a[class ="shopping_cart_link"]')
PICKED_ITEM_1 = ('xpath','//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]')
RMV_FROM_CART_BTN_1 = ('xpath', '//button[@id="remove-sauce-labs-backpack"]')
ADD_BOLT_T_SHIRT_ITEM = ('xpath', '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
ADD_RED_T_SHIRT_ITEM = ('xpath', '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')
CART_TAG_ICON = '<span class="shopping_cart_badge" data-test="shopping-cart-badge"></span>'
RMV_BOLT_T_SHIRT_ITEM = ('xpath', '//button[@id="remove-sauce-labs-bolt-t-shirt"]')
RMV_RED_T_SHIRT_ITEM = ('xpath', '//button[@class="btn btn_secondary btn_small cart_button"]')
ITEM_TITLE_3 = ('xpath', '(//div[@data-test="inventory-item-name"])[1]')
ITEM_TITLE_4 = ('xpath', '//a[@id="item_4_title_link"]')
CARD_ITEM_TITLE_3 = ('xpath', '//div[@data-test="inventory-item-name"]')
ADD_TO_CART_BTN = ('xpath', '//button[@id="add-to-cart"]')
RMV_FROM_CART_BTN = ('xpath', '//button[@id="remove"]')

# ITEM CARD
ITEM_IMG = ('xpath', '//a[@id="item_0_img_link"]/img')
ITEM_DESC = ('xpath', '(//div[@class="inventory_item_desc"])[2]')
ITEM_CARD_DESC = ('xpath', '//div[@data-test="inventory-item-desc"]')
ITEM_TITLE = ('xpath', '//a[@id="item_1_title_link"]/div')
ITEM_DESC_1 = ('xpath', '(//div[@class="inventory_item_desc"])[3]')
ITEM_CARD_DESC_1 = ('xpath', '//div[@data-test="inventory-item-desc"]')

# ORDER
ADD_FLEECE_ITEM = ('xpath', '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
CHECKOUT_BTN = ('xpath', '//button[@data-test="checkout"]')
F_NAME_FIELD = ('xpath', '//input[@data-test="firstName"]')
L_NAME_FIELD = ('xpath', '//input[@data-test="lastName"]')
ZIPCODE_FIELD = ('xpath', '//input[@data-test="postalCode"]')
CONTINUE_BTN = ('xpath', '//input[@id="continue"]')
FINISH_BTN = ('xpath', '//button[@id="finish"]')

# FILTER
A_TO_Z_FILTER = ('xpath', '//option[@value="az"]')
Z_TO_A_FILTER = ('xpath', '//option[@value="za"]')
ITEM_PRICE_LIST = ('xpath', '//div[@class="inventory_item_price"]')
LOW_TO_HIGH_FILTER = ('xpath', '//option[@value="lohi"]')
HIGH_TO_LOW_FILTER = ('xpath', '//option[@value="hilo"]')

# BURGER MENU
BURGER_BTN = ('id', 'react-burger-menu-btn')
LOGOUT_BTN = ('css selector', '#logout_sidebar_link')
ABOUT_BTN = ('css selector', '#about_sidebar_link')
RESET_BTN = ('css selector', '#reset_sidebar_link')
