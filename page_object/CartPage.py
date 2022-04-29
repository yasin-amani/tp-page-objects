from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class CartPage:
    SelectionerQuantite = "select[name='quantity']"
    QuantiteCible = "2"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def changeQuantity(self, quantity):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.SelectionerQuantite)))
        selecteurQuantite = Select(self.driver.find_element(By.CSS_SELECTOR, self.SelectionerQuantite))
        selecteurQuantite.select_by_value(quantity)

        return selecteurQuantite.first_selected_option.text

