# from selenium.webdriver.common.alert import Alert

# from MainPage import MainPage



# def test_search_input(driver):
#     MainPage(driver).click_search("test")




from ch3 import MainStr, StrProduct, StrRegistrathion, Cart, WishList, Answear


# # 0 Проверка работы кода
# def test_code_is_working(browser):
#     browser.get("http://localhost/")

# 1 Проверка изменения валюты
def test_MainStr_change_the_valute(browser):
    mainstr_is_valuta = MainStr(browser)
    # mainstr_is_valuta.go_to_site()
    mainstr_is_valuta.change_the_valute()
    #assert

# # 2 Проверка поисковой строки на главной страницы
# def test_MainStr_poisk(browser):
#     mainstr_poisk = MainStr(browser)
#     mainstr_poisk.go_to_site()
#     mainstr_poisk.poisk()
#     #assert

# # 3 Проверка сцены изобраденний товара
# def test_StrProduct_check_the_product(browser):
#     check_scroll_img = StrProduct(browser)
#     check_scroll_img.go_to_site()
#     check_scroll_img.check_the_product()
#     #assert

# # 4 проверка что страница PC пуста
# def test_StrProduct_check_the_pc(browser):
#     check_on_null = StrProduct(browser)
#     check_on_null.go_to_site()
#     check_on_null.check_the_pc()
#     #assert

# # 5 Проверка регистрации
# def test_StrRegistrathion_registration(browser):
#     registration = StrRegistrathion(browser)
#     registration.go_to_site()
#     registration.registration()
#     #assert

# # 6 Проверка добавления камеры в карзину
# def test_Cart_click_product_camera(browser):
#     cart_camera = Cart(browser)
#     cart_camera.go_to_site()
#     cart_camera.click_product(4)
#     #assert

# # 7  Проверка добавления телефона в карзину
# def test_Cart_click_product_phone(browser):
#     cart_phone = Cart(browser)
#     cart_phone.go_to_site()
#     cart_phone.click_product(2)
#     #assert

# # 8Проверка добавления планшета в карзину
# def test_Cart_click_product_pad(browser):
#     cart_pad = Cart(browser)
#     cart_pad.go_to_site()
#     cart_pad.click_product(1)
#     #assert

# # 9 Проверка добавления продукта в избранные
# def test_WishList_click_product(browser):
#     wishlist_product = WishList(browser)
#     # wishlist_product.go_to_site()
#     wishlist_product.click_product()
#     #assert

# # 10 Проверка отзыва
# def test_Answear_click(browser):
#     answer_product = Answear(browser)
#     # answer_product.go_to_site()
#     answer_product.click()
#     #assert
