from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = ""
password = ""
url = "https://brainly.co.id/"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

login_selecotr = "//a[@href='/login?entry=2']"
username_selector = "//input[@name='username']"
password_selector = "//input[@name='password']"
login_button_selector = "//button[@data-test='form-login-submit']"
blue_button_selecotr = (By.XPATH, '//*[@class="sg-button sg-button--small sg-button--primary-blue sg-button--full-width"]')

driver.find_element_by_xpath(login_selecotr).click()
driver.find_element_by_xpath(username_selector).send_keys(username)
driver.find_element_by_xpath(password_selector).send_keys(password + Keys.ENTER)

#driver.find_element_by_xpath(login_button_selector).click()

blue_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(blue_button_selecotr))
blue_button.click()

driver.quit()
