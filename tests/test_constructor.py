import pytest
from constants.locators import TestLocators
from constants.constants import TestUrlConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    @pytest.mark.usefixtures('driver')
    def test_from_my_account_to_constructor(self, driver):

        driver.get(TestUrlConstants.MAIN_PAGE_URL)

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOC).click()

        email = driver.find_element(*TestLocators.EMAIL_INPUT_LOC)
        password = driver.find_element(*TestLocators.PASSWORD_INPUT_LOC)

        email.click()
        email.clear()
        email.send_keys('peleeva5@gmail.com')

        password.click()
        password.clear()
        password.send_keys('pew123!')

        driver.find_element(*TestLocators.LOG_IN_LOC).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOC).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.PROFILE_PAGE_URL))

        driver.find_element(*TestLocators.CONSTRUCTOR_LOC).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.MAIN_PAGE_URL))

    @pytest.mark.usefixtures('driver')
    def test_constructor_categories(self, driver):

        driver.get(TestUrlConstants.MAIN_PAGE_URL)

        pastry = driver.find_element(*TestLocators.PASTRY_LOC)
        souces = driver.find_element(*TestLocators.SOUCES_LOC)
        fillings = driver.find_element(*TestLocators.FILLINGS_LOC)

        souces.click()

        assert WebDriverWait(driver, 5).until(
                    expected_conditions.visibility_of_element_located(TestLocators.SOUCES_LOC))

        fillings.click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_LOC))

        pastry.click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PASTRY_LOC))
