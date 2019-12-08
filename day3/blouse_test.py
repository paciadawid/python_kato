import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import *


class BlouseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        #self.driver.implicitly_wait(3)

    def test_total_price(self):
        search_selector = "search_query_top"
        loop_selector = "submit_search"
        search_text = "blouse"
        add_to_cart_selector = "//a[@title='Add to cart']"
        product_container_selector = "product-container"
        proceed_to_checkout_selector = (By.XPATH, "//a[@title='Proceed to checkout']")
        blouse_price_selector = "//div[@class='right-block']/*/*[@itemprop='price']"
        total_price_selector = (By.XPATH, "//td[@id='total_product']")

        self.driver.find_element_by_id(search_selector).send_keys(search_text)
        self.driver.find_element_by_name(loop_selector).click()
        blouse_price = self.driver.find_element_by_xpath(blouse_price_selector).text
        print(blouse_price)
        blouse = self.driver.find_element_by_class_name(product_container_selector)
        ActionChains(self.driver).move_to_element(blouse).perform()
        self.driver.find_element_by_xpath(add_to_cart_selector).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(proceed_to_checkout_selector)).click()
        total_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(total_price_selector)).text
        #self.driver.find_element_by_xpath(proceed_to_checkout_selector).click()
        print(blouse_price, total_price)
        assert_that(blouse_price, equal_to(total_price))
        total_shipping_selector = "//td[@id='total_shipping']"
        total_shipping_cost = self.driver.find_element_by_xpath(total_shipping_selector).text
        assert_that(float(total_shipping_cost[1:]), equal_to(0.0))

    def tearDown(self):
       pass
       self.driver.quit()


if __name__ == '__main__':
    unittest.main()
