import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestProductDetails:

    @pytest.mark.product_details
    def test_verify_product_image(self, driver, locator=None):
        driver.get("https://demo.opencart.com/")
        driver.implicitly_wait(10)
        thumbnail_image = driver.find_element(By.XPATH, "//img[@alt='iPhone 6']")
        thumbnail_image.click()
        samsung = driver.find_element(By.XPATH, "(//h1[normalize-space()='Samsung Galaxy Tab 10.1'])[1]")
        assert samsung == "Samsung Galaxy Tab 10.1"

    @pytest.mark.product_details
    def test_add_to_cart_button(self, driver):
        driver.get("https://demo.opencart.com/")
        thumbnail_image = driver.find_element(By.XPATH, "//img[@alt='iPhone 6']")
        thumbnail_image.click()
        add_to_cart_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]")
        add_to_cart_button.click()
        message = driver.find_element(By.XPATH, "(//div[@id='alert'])[1]").text
        assert message == " Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!"
