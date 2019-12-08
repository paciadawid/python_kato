from selenium import webdriver
from day3.PoP_tests.locators.main_selectors import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product):
        self.driver.find_element(*search_field_selector).send_keys(product)
        self.driver.find_element(*loop_selector).click()
