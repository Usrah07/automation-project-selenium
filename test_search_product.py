from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_search_product():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(3)
    driver.find_element(By.ID, "search_product").send_keys("Top")
    driver.find_element(By.ID, "submit_search").click()
    time.sleep(2)
    assert "Searched Products" in driver.page_source
    driver.quit()
