import unittest
from selenium import webdriver
from day3.PoP_tests.pages.main_page import MainPage
from day3.PoP_tests.pages.search_page import SearchPage

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_something(self):
        self.main_page.search_product("blouse")
        product_price = self.search_page.get_product_price()
        self.search_page.add_product_to_cart()
        self.search_page.proceed_to_checkout()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
