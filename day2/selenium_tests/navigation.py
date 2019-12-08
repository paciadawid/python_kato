from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from hamcrest import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")

css_selector_banner = (By.CSS_SELECTOR, "a > img[class='img-responsive']")
xpath_selector_banner = (By.XPATH, "//a/img[@class='img-responsive']")


banner_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(css_selector_banner))

search_field = driver.find_element_by_id("search_query_top")
loop_button = driver.find_element_by_name("submit_search")

search_text = "test"

search_field.send_keys(search_text)
loop_button.click()

warning = driver.find_element_by_css_selector("p[class='alert alert-warning']")
warning_text = warning.text

assert_that(warning_text, ("No results were found for your search"))

driver.quit()
