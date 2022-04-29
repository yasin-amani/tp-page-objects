from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmationPage:
    AllerAuPanier = "a.a-button-text"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def openCart(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.AllerAuPanier)))
        self.driver.find_element(By.CSS_SELECTOR, self.AllerAuPanier).click()