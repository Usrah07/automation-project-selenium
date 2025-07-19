from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()
    assert "Shopping Cart" in driver.page_source
    driver.quit()
