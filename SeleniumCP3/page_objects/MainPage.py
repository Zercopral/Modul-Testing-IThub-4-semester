from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):

    CURRENCY_LIST_OPEN = (By.CSS_SELECTOR, "a.dropdown-toggle > i.fa-caret-down")
    CURRENCY_LIST_DATA = (By.CSS_SELECTOR, "ul.show > li")
    CURRENCY_CURRENT = (By.CSS_SELECTOR, "#form-currency > div.dropdown > a > strong")
    # 2.	Сменить валюту на главной странице с доллара на евро и обратно.

    def change_the_currency(self, index):
        self.element(self.CURRENCY_LIST_OPEN).click()
        self.elements(self.CURRENCY_LIST_DATA)[index].click()
    
    def get_current_currency(self):
        return self.element(self.CURRENCY_CURRENT).text
    

    # 1.	Кликнуть на продукт на главной странице, проверить переключение скриншотов на странице с продуктом.
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.description > h4 > a")

    def choose_featured_product(self, index):
        selected_product = self.elements(self.FEATURED_PRODUCTS)[index]
        return selected_product.find_element(*self.PRODUCT_LINK)


    def click_featured_product(self, index):
        self.choose_featured_product(index).click()

        
    def get_featured_product_name(self, index):
        return self.choose_featured_product(index).text
    

    # # 3.	Перейти через меню в категорию PC, проверить, что страница пуста.

    OPEN_MENU = (By.CSS_SELECTOR, "#narbar-menu > ul > li")
    LINKS_OPENED_MENU = (By.CSS_SELECTOR, "div.dropdown-menu.show > div.dropdown-inner > .list-unstyled > li")


    def open_menu(self, index):
        self.elements(self.OPEN_MENU)[index].click()

    def go_to_category_in_menu(self, index):
        self.elements(self.LINKS_OPENED_MENU)[index].click()
    

    # 4.	Пройти через меню в регистрацию, заполнить все поля и нажать «зарегистрироваться».

    TOP_RIGHT_MENU = (By.CSS_SELECTOR, "div.nav.float-end > ul > li")
    OPENED_MENU = (By.CSS_SELECTOR, "ul.show > li")

    def go_to_register_page(self):
        self.elements(self.TOP_RIGHT_MENU)[1].click()
        self.elements(self.OPENED_MENU)[0].click()

    
    # 5.	Написать в строке поиска на главной странице поисковое слово и нажать кнопку поиска (может выдать ошибку).

    INPUT_SEARCH = (By.CSS_SELECTOR, "input[name='search']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search > button")

    def search(self, search_word):
        try:
            self._input(self.element(self.INPUT_SEARCH), search_word)
            self.click(self.element(self.BUTTON_SEARCH))
        except Exception as e:
            pass
    
    # 6.    Добавление товара в вишлист
        
    def go_to_Login_Page(self):
        self.elements(self.TOP_RIGHT_MENU)[1].click()
        self.elements(self.OPENED_MENU)[1].click()

    WISHLIST_PAGE = (By.CSS_SELECTOR, "#wishlist-total")

    def go_to_Wishlist_Page(self):
        self.click(self.element(self.WISHLIST_PAGE))

    BUTTON_ADD_TO_WISHLIST = (By.CSS_SELECTOR, ".button-group > button:nth-child(2)")

    def add_featured_product_to_wishlist(self, featured_product_index):
        self.elements(self.BUTTON_ADD_TO_WISHLIST)[featured_product_index].click()
    
  