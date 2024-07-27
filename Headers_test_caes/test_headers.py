import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestHeaders:

    @pytest.mark.headers
    def test_search_input(self, driver, locator=None):
        driver.get("https://demo.opencart.com/")
        search_input = driver.find_element(By.XPATH, "(//input[@placeholder='Search'])[1]")
        search_input.click()
        search_input.send_keys("iphone")
        driver.find_element(By.XPATH, "(//button[@class='btn btn-light btn-lg'])[1]").click()
        time.sleep(5)
        iphone = driver.find_element(By.XPATH, "(//a[normalize-space()='iPhone'])[1]")
        assert iphone.is_displayed()

    @pytest.mark.headers
    def test_cart_is_visible(self, driver):
        driver.get("https://demo.opencart.com/")
        shopping_cart = driver.find_element(By.XPATH, "(//button[normalize-space()='0 item(s) - $0.00'])[1]")
        assert shopping_cart.is_displayed()
