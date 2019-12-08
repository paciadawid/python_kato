import unittest
from selenium import webdriver
from day3.PoP_tests.pages.main_page import MainPage
from day3.PoP_tests.pages.search_page import SearchPage
from day3.PoP_tests.pages.summary_page import SummaryPage
from hamcrest import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.summary_page = SummaryPage(self.driver)

    def test_something(self):
        self.main_page.search_product("blouse")
        product_price = self.search_page.get_product_price()
        self.search_page.add_product_to_cart()
        self.search_page.proceed_to_checkout()
        total_price = self.summary_page.get_total_price()
        shpping_price = self.summary_page.get_shipping_price()

        assert_that(product_price, is_(total_price))
        assert_that(shpping_price, is_(2.0))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
