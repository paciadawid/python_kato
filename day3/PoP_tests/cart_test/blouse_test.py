import unittest
from selenium import webdriver
from day3.PoP_tests.pages.main_page import MainPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.main_page = MainPage(self.driver)

    def test_something(self):
        self.main_page.search_product("blouse")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
