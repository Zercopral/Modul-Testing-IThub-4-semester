from appium.webdriver.common.appiumby import AppiumBy

class AppCalculator:

    def __init__(self, driver) -> None:
        self.driver = driver

    math_basic_operator = {
        "+":'//android.widget.Button[@content-desc="plus"]',
        "-":'//android.widget.Button[@content-desc="minus"]',
        "*":'//android.widget.Button[@content-desc="×"]',
        "/":'//android.widget.Button[@content-desc="divide"]'
    }

    numbers = {
        "0":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_0"]',
        "1":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_1"]',
        "2":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_2"]',
        "3":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_3"]',
        "4":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]',
        "5":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_5"]',
        "6":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_6"]',
        "7":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_7"]',
        "8":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_8"]',
        "9":'//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_9"]'
    }

    clean_button = '//android.widget.Button[@content-desc="clear"]'
    equals_button = '//android.widget.Button[@content-desc="equals"]'

    calc_result = '//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_final"]'


    def __enter_number(self, number):
        for sign in number:
            self.driver.find_element(by=AppiumBy.XPATH, value=self.numbers[sign]).click()


    def __enter_operator(self, operator):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.math_basic_operator[operator]).click()


    def __click_equal(self):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.equals_button).click()
    

    def __get_result(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value=self.calc_result).text
    

    def __clear(self):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.clean_button).click()
    

    def calc_expression(self, *expression):
        for elem in expression:

            if elem.isdigit():
                self.__enter_number(elem)
            
            elif elem in list(self.math_basic_operator.keys()):
                self.__enter_operator(elem)
            
        self.__click_equal()
        output = self.__get_result()
        self.__clear()

        return output