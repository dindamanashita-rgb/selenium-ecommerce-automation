from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open Chrome
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

# 2. Login
driver.find_element(By.XPATH, "//span[text()='My Account']").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(2)

driver.find_element(By.ID, "input-email").send_keys(
    "manashrita12345@testmail.com"
)

driver.find_element(By.ID, "input-password").send_keys(
    "manashrita@2004"
)

driver.find_element(
    By.XPATH, "//input[@value='Login']"
).click()

time.sleep(4)

print("Login successful")


# 3. Search iPhone
search = driver.find_element(By.NAME, "search")
search.send_keys("iPhone")

driver.find_element(
    By.CSS_SELECTOR,
    "button.btn.btn-default.btn-lg"
).click()

time.sleep(4)

print("iPhone search completed")


# 4. Open iPhone
driver.find_element(
    By.XPATH,
    "//div[@class='caption']//h4/a"
).click()

time.sleep(4)

print("iPhone product page opened")


# 5. Add to Cart
driver.execute_script(
    "document.getElementById('button-cart').click();"
)

time.sleep(4)

print("Product added to cart")


# 6. Open Cart
driver.get(
    "https://tutorialsninja.com/demo/index.php?route=checkout/cart"
)

time.sleep(4)

print("Shopping cart opened")


# 7. Checkout
driver.find_element(
    By.LINK_TEXT,
    "Checkout"
).click()

time.sleep(4)

print("Checkout page opened")

print("TEST COMPLETED")

time.sleep(10)

driver.quit()