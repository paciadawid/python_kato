from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_css_selector("img[alt='My Store']")
driver.quit()
