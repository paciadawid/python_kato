from selenium import webdriver


class MainPage:

    search_field_selector = "search_query_top"
    loop_selector = "submit_search"

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product):
        self.driver.find_element_by_id(self.search_field_selector).send_keys(product)
        self.driver.find_element_by_name(self.loop_selector).click()
