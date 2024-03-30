## Autotests for Swag Labs site  

# Site URL: https://www.saucedemo.com/  
Функционал, который необходимо покрыть автотестами:  
## Авторизация:  
tes_auth.py  
1. Авторизация используя корректные данные (standard_user, secret_sauce): case 1.1  
2. Авторизация используя некорректные данные (user, user): case 1.2 
  
## Корзина:
test_cart.py  
1. Добавление товара в корзину через каталог: case 2.1  
2. Удаление товара из корзины через корзину: case 2.2  
3. Добавление товара в корзину из карточки товара: case 2.3  
4. Удаление товара из корзины через карточку товара: case 2.4  
  
## Карточка товара:  
test_item_card.py  
1. Успешный переход к карточке товара после клика на картинку товара: case 3.1  
2. Успешный переход к карточке товара после клика на название товара: case 3.2  
  
## Оформление заказа:  
test_order.py  
1. Оформление заказа используя корректные данные: case 4.1  
  
## Фильтр:  
test_filter.py  
1. Проверка работоспособности фильтра (A to Z): case 5.1  
2. Проверка работоспособности фильтра (Z to A): case 5.2  
3. Проверка работоспособности фильтра (low to high): case 5.3  
4. Проверка работоспособности фильтра (high to low): case 5.4  
  
## Бургер меню:  
test_menu.py  
1. Выход из системы: case 6.1  
2. Проверка работоспособности кнопки "About" в меню: case 6.2  
3. Проверка работоспособности кнопки "Reset App State": case 6.3  
4. Негативная проверка кнопки: case 6.4 DEFECT FOUND  