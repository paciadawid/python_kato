from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    product_container_selector = "product-container"
    add_to_cart_selector = "//a[@title='Add to cart']"
    proceed_to_checkout_selector = (By.XPATH, "//a[@title='Proceed to checkout']")
    product_price_selector = "//div[@class='right-block']/*/*[@itemprop='price']"

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        product = self.driver.find_element_by_class_name(self.product_container_selector)
        ActionChains(self.driver).move_to_element(product).perform()
        self.driver.find_element_by_xpath(self.add_to_cart_selector).click()

    def get_product_price(self):
        product_price = self.driver.find_element_by_xpath(self.product_price_selector).text
        return product_price

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.proceed_to_checkout_selector)).click()
