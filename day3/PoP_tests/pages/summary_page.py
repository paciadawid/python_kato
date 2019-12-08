from selenium import webdriver
from day3.PoP_tests.locators.summary_locators import *

class SummaryPage:



    def __init__(self, driver):
        self.driver = driver

    def get_shipping_price(self):
        shipping_cost = self.driver.find_element(*total_shipping_selector).text
        shipping_cost = float(shipping_cost[1:])
        return shipping_cost

    def get_total_price(self):
        total_price = self.driver.find_element(*total_price_selector).text
        return total_price
