from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class SearchPage(BasePage):

    PRODUCT_LINK = (By.CSS_SELECTOR, ".description > h4:nth-child(1) > a:nth-child(1)")

    def click_on_product(self):
        self.logger.info("Click on a product")
        self.click(self.element(self.PRODUCT_LINK))