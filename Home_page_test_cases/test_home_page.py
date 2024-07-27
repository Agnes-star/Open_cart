import pytest
from selenium.webdriver.common.by import By


class TestHomePage:

    @pytest.mark.home_page
    def test_home_page_title(self, driver):
        driver.get("https://demo.opencart.com/")
        title = driver.title
        assert title == "Your Store"

    @pytest.mark.home_page
    def test_main_banner_displayed(self, driver):
        driver.get("https://demo.opencart.com/")
        main_banner = driver.find_element(By.XPATH, "(//img[@title='Your Store'])[1]")
        assert main_banner.is_displayed()

    @pytest.mark.home_page
    def test_navigation_to_featured_product(self, driver):
        driver.get("https://demo.opencart.com/")
        driver.find_element(By.XPATH, "(//a[normalize-space()='iPhone'])[1]").click()
        assert driver.find_element(By.XPATH,
                                   "(//h1[normalize-space()='iPhone'])[1]").text == "iPhone"
