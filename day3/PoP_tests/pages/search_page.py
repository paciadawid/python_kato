from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day3.PoP_tests.locators.search_selectors import *


class SearchPage:


    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        product = self.driver.find_element(*product_container_selector)
        ActionChains(self.driver).move_to_element(product).perform()
        self.driver.find_element(*add_to_cart_selector).click()

    def get_product_price(self):
        product_price = self.driver.find_element(*product_price_selector).text
        return product_price

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(proceed_to_checkout_selector)).click()
