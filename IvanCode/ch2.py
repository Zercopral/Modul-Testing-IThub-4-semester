from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
import os

options = webdriver.ChromeOptions()
useragent = UserAgent()

options.add_argument(f"user-agent={useragent.chrome}")
options.add_argument("--disable-blink-features=AutomationControlled")

exec_path = os.path.join("C:\chromedriver\chromedriver.exe") # у тебя слишком новый chrome браузер

driver = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, executable_path=exec_path))

# проходим каппчу
def check_capcha():

    while driver.title == 'Один момент…':
        print("Мы в капче...")
        iframe = driver.find_element(By.CSS_SELECTOR, '#turnstile-wrapper > div > iframe')
        driver.switch_to.frame(iframe)

        driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/label/input').click()
        print("Прошёл капчу")
        driver.switch_to.default_content()
        time.sleep(13)

    print(driver.title)


# 1.	Кликнуть на продукт на главной странице, проверить переключение скриншотов на странице с продуктом.

def check_the_product():

        print("Тыкаем на товар")
        driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[2]/div[1]/form/div/div[1]/a/img').click()
        time.sleep(5)
        print("Тыкаем на картинку товара")
        driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[1]/div[1]/div/a/img').click()
        time.sleep(5)
        print("Меняем слайд")
        sckrol = driver.find_element(By.XPATH, '/html/body/div[2]/div/button[2]')
        sckrol.click()
        time.sleep(5)

        while True:

            try:
                click_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/button')
                print("Выходим из режима просмотра")
                click_button.click()
                break
            except Exception as ex:

                print("Меняем слайд")
                sckrol.click()
                time.sleep(5)

        time.sleep(5)
        print("Возвращаемся на главную страницу")
        driver.find_element(By.XPATH, '/html/body/header/div/div/div[1]/div/a/img').click()
        time.sleep(5)


# 2.	Сменить валюту на главной странице с доллара на евро и обратно.
def change_the_valute():

    print("Выбираем меню с валютой")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/a/i').click()
    time.sleep(5)
    print("Выбираем евро")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/ul/li[1]/a').click()
    time.sleep(5)
    print("Выбираем меню с валютой")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/a/i').click()
    time.sleep(5)
    print("Выбираем долар")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li[1]/form/div/ul/li[3]/a').click()
    time.sleep(5)

# 3.	Перейти через меню в категорию PC, проверить, что страница пуста.
def check_the_pc():

    # print("Нажимаем на главное меню")
    # driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/button').click()
    # time.sleep(5)
    print("выбираем Desktops")
    driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[1]/a').click()
    time.sleep(5)
    print("Выбираем PC")
    driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a').click()
    time.sleep(5)

    try:
        print("Проверям на пустоту")
        p_body = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/p')
        if (p_body):
            if (p_body.text == "There are no products to list in this category."):
                print("Товаров нет")
        else: print("Товары в наличии")
        time.sleep(5)
    except Exception as ex:
        print(ex)

    print("Возвращаемся на главную страницу")
    driver.find_element(By.XPATH, '/html/body/header/div/div/div[1]/div/a/img').click()
    time.sleep(5)
    
# 4.	Пройти через меню в регистрацию, заполнить все поля и нажать «зарегистрироваться».
def registration():

    print("Нажимаем на главное меню")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/a/i[2]').click()
    time.sleep(5)
    print("выбираем регистрацию")
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a').click()
    time.sleep(5)
    print("заполняем поля")
    input_name = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/input')
    input_name.send_keys("Иван")
    time.sleep(5)
    input_sername = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/input')
    input_sername.send_keys("Сайгин")
    time.sleep(5)
    input_email = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[1]/div[4]/div/input')
    input_email.send_keys("123@mail.ru")
    time.sleep(5)
    input_pessword = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/input')
    input_pessword.send_keys("1234")
    time.sleep(5)
    print("Выбираем рассылку")
    driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/fieldset[3]/div/div/div[1]/input').click()
    time.sleep(5)
    print("Соглашаемся с обработкой перснональных данных")
    driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/div/div/div/input').click()
    time.sleep(5)
    print("Создаем аккаунт")
    driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/form/div/div/button').click()
    time.sleep(5)
    print("Возвращаемся на главную страницу")
    driver.find_element(By.XPATH, '/html/body/header/div/div/div[1]/div/a/img').click()
    time.sleep(5)

    

    
# 5.	Написать в строке поиска на главной странице поисковое слово и нажать кнопку поиска (может выдать ошибку).
def poisk():

    print("Вводим значение в поисковую строку")
    input_str = driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/input')
    input_str.send_keys("Mac")
    time.sleep(5)
    print("нажимаем поиск")
    driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/button')
    time.sleep(5)


try:

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
    })

    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    time.sleep(10)
    print(driver.title)

    check_capcha()
    check_the_product()
    change_the_valute()
    check_the_pc()
    registration()
    poisk()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()





