from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CategoryPage(BasePage):

    EMPTY_CONTENT = (By.CSS_SELECTOR, "#content > p")

    def get_empty_content(self):
        return self.element(self.EMPTY_CONTENT).text