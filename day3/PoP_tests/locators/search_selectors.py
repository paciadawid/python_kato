from selenium.webdriver.common.by import By

product_container_selector = (By.CLASS_NAME, "product-container")
add_to_cart_selector = (By.XPATH, "//a[@title='Add to cart']")
proceed_to_checkout_selector = (By.XPATH, "//a[@title='Proceed to checkout']")
product_price_selector = (By.XPATH, "//div[@class='right-block']/*/*[@itemprop='price']")

