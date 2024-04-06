from base_url import BasePage 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MainStr(BasePage):

    FIND_LIST = (By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/a/i')
    FIND_EVRO = (By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/ul/li[1]/a')
    FIND_DOLLAR = (By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/ul/li[3]/a')
    INPUT_STR = (By.XPATH, '/html/body/header/div/div/div[2]/div/input')
    SOURCH = (By.XPATH, '/html/body/header/div/div/div[2]/div/button')
    MAIN_STR = (By.XPATH, '/html/body/header/div/div/div[1]/div/a/img')

    def change_the_valute(self):

        print("Выбираем меню с валютой")
        find_list = self.driver.find_element(*self.FIND_LIST).click()
        time.sleep(5)
        print("Выбираем евро")
        find_evro = self.driver.find_element(*self.FIND_EVRO).click()
        time.sleep(5)
        print("Выбираем меню с валютой")
        find_list = self.driver.find_element(*self.FIND_LIST).click()
        time.sleep(5)
        print("Выбираем долар")
        find_dollar = self.driver.find_element(*self.FIND_DOLLAR).click()
        time.sleep(5)
    
    def poisk():

        print("Вводим значение в поисковую строку")
        input_str = self.driver.find_element(*self.INPUT_STR)
        input_str.send_keys("Mac")
        time.sleep(5)
        print("нажимаем поиск")
        sourch = self.driver.find_element(*self.SOURCH)
        time.sleep(5)

    def Back_main_str(self):

        main_str = self.driver.find_element(*self.MAIN_STR).click()




class StrProduct(BasePage):

    PRODUCT = (By.XPATH, '/html/body/main/div[2]/div/div/div[2]/div[1]/form/div/div[1]/a/img')
    IMG = (By.XPATH, '/html/body/main/div[2]/div/div/div[1]/div[1]/div/a/img')
    SCROL = (By.XPATH, '/html/body/div[2]/div/button[2]')
    BUTTON = (By.XPATH, '/html/body/div[2]/div/div[1]/div/button')
    DESKTOP = (By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[1]/a')
    PC = (By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a')
    BODY = (By.XPATH, '/html/body/main/div[2]/div/div/p')

    def check_the_product():

        print("Тыкаем на товар")
        product = self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("Тыкаем на картинку товара")
        img = self.driver.find_element(*self.IMG).click()
        time.sleep(5)
        print("Меняем слайд")
        sckrol  = self.driver.find_element(*self.SCROL).click()
        time.sleep(5)

        while True:

            try:
                button =  self.driver.find_element(*self.BUTTON).click()
                print("Выходим из режима просмотра")
                break
            except Exception as ex:

                print("Меняем слайд")
                sckrol.click()
                time.sleep(5)

        time.sleep(5)
        MainStr().Back_main_str()
        time.sleep(5)


    def check_the_pc():


        print("выбираем Desktops")
        desktop  = self.driver.find_element(*self.DESKTOP).click()
        time.sleep(5)
        print("Выбираем PC")


        pc  = self.driver.find_element(*self.PC).click()
        time.sleep(5)

        try:
            print("Проверям на пустоту")
            if (self.BODY):
                if (self.BODY.text == "There are no products to list in this category."):
                    print("Товаров нет")
            else: print("Товары в наличии")
            time.sleep(5)
        except Exception as ex:
            print(ex)

        print("Возвращаемся на главную страницу")
        MainStr().Back_main_str()
        time.sleep(5)

class StrRegistrathion(BasePage):

    MAIN_MENU = (By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/a/i[2]')
    REGISTRATHION = (By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a')
    NAME = (By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/input')
    LASTNAME = (By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/input')
    EMAIL = (By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[4]/div/input')
    PASSWORD = (By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/input')
    SMS = (By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[3]/div/div/div[1]/input')
    PERSONAL_DATA = (By.XPATH, '/html/body/main/div[2]/div/div/form/div/div/div/input')
    CREATE_ACCAUNT = (By.XPATH, '/html/body/main/div[2]/div/div/form/div/div/button')


    def registration():

        print("Нажимаем на главное меню")
        self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("выбираем регистрацию")
        self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("заполняем поля")
        NAME.send_keys("Иван")
        time.sleep(5)
        LASTNAME.send_keys("Сайгин")
        time.sleep(5)
        EMAIL.send_keys("123@mail.ru")
        time.sleep(5)
        PASSWORD.send_keys("1234")
        time.sleep(5)
        print("Выбираем рассылку")
        sms = self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("Соглашаемся с обработкой перснональных данных")
        personal_data = self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("Создаем аккаунт")
        create_accaunt = self.driver.find_element(*self.PRODUCT).click()
        time.sleep(5)
        print("Возвращаемся на главную страницу")
        MainStr().Back_main_str()
        time.sleep(5)


class Cart(BasePage):

    ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4")


    def click_product(self, indexs):

        feature_product = self.driver.find_element(*self.ADD_PRODUCT)
        dop_path =  f' > div:nth-child({index}) > div > div.content > form > div > button:nth-child(1)'
        concat_path = ADD_PRODUCT[1] + dop_path
        print(concat)
        feature_product.find_element(By.CSS_SELECTOR, "> div > div.content > form > div > button:nth-child(1)").click()
        MainStr().Back_main_str()

class WishList(BasePage):

    ADD_LIKE_PRODUCT = (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4")

    def click_product(self, indexs):

        feature_product = self.driver.find_element(*self.ADD_LIKE_PRODUCT)
        dop_path =  f' > div:nth-child({index}) > div > div.content > form > div > button:nth-child(2)'
        concat_path = ADD_PRODUCT[1] + dop_path
        print(concat)
        feature_product.find_element(By.CSS_SELECTOR, "> div > div.content > form > div > button:nth-child(1)").click()
        MainStr().Back_main_str()

class Answear(BasePage):

    PRODUCT = (By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.image > a")
    REVIEW = (By.CSS_SELECTOR,"#content > ul > li:nth-child(3) > a")
    INPUT_NAME = (By.CSS_SELECTOR, '#input-name')
    INPUT_REVIEW = (By.CSS_SELECTOR, '#input-text')
    PATING = (By.CSS_SELECTOR, '#input-rating')
    CONTINUE = (By.CSS_SELECTOR, '#button-review')

    def click(self):

       feature_product = self.driver.find_element(*self.PRODUCT).click()
       feature_product = self.driver.find_element(*self.REVIEW).click()

       input_name = self.driver.find_element(*self.INPUT_NAME)
       input_name.send_keys("Иван")

       input_review = self.driver.find_element(*self.INPUT_REVIEW)
       input_review.send_keys("ЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙЙ")

       input_rating = self.driver.find_element(*self.INPUT_REVIEW).click()

       button_review = self.driver.find_element(*self.CONTINUE).click()
       MainStr().Back_main_str()
