from selenium import webdriver
from hamcrest import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")

search_selector = "search_query_top"
loop_selector = "submit_search"
warning_selector = "p[class='alert alert-warning']"

search_field = driver.find_element_by_id(search_selector)
loop_button = driver.find_element_by_name(loop_selector)

search_text = "test"

search_field.send_keys(search_text)
loop_button.click()

warning = driver.find_element_by_css_selector(warning_selector)
warning_text = warning.text

assert_that(warning_text, ("No results were found for your search"))

driver.quit()
