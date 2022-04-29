from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    AjouterAuPanier = "#add-to-cart-button.a-button-input"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def addToCart(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.AjouterAuPanier)))
        self.driver.find_element(By.CSS_SELECTOR, self.AjouterAuPanier).click()