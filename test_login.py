from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("automationtestuser@email.com")
    driver.find_element(By.NAME, "password").send_keys("test1234")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    assert "Logged in as" in driver.page_source
    driver.find_element(By.LINK_TEXT, "Logout").click()
    assert "Login to your account" in driver.page_source
    driver.quit()
