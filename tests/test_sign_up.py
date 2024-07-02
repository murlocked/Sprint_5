import pytest
from constants.constants import TestUrlConstants
from constants.locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSignUp:

    @pytest.mark.usefixtures('driver')
    def test_sign_up_incorrect_password(self, driver):
        driver.get(TestUrlConstants.MAIN_PAGE_URL)
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOC).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.LOG_IN_PAGE_URL))

        driver.find_element(*TestLocators.SIGN_UP_FROM_LOG_IN_PAGE_LOC).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.SIGN_UP_PAGE_URL))

        name = driver.find_element(*TestLocators.NAME_INPUT_LOC)
        email = driver.find_element(*TestLocators.EMAIL_INPUT_LOC)
        password = driver.find_element(*TestLocators.PASSWORD_INPUT_LOC)

        name.click()
        name.clear()
        name.send_keys('Anya')

        email.click()
        email.clear()
        email.send_keys('peleeva55555@gmail.com')

        password.click()
        password.clear()
        password.send_keys('123')

        driver.find_element(*TestLocators.SIGN_UP_CONFIRMATION_LOC).click()

        assert driver.find_element(*TestLocators.INCORRECT_PASSWORD_MSG_LOC)

    @pytest.mark.usefixtures('driver')
    def test_sign_up_correct_password(self, driver):
        driver.get(TestUrlConstants.MAIN_PAGE_URL)
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOC).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.LOG_IN_PAGE_URL))

        driver.find_element(*TestLocators.SIGN_UP_FROM_LOG_IN_PAGE_LOC).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.SIGN_UP_PAGE_URL))

        name = driver.find_element(*TestLocators.NAME_INPUT_LOC)
        email = driver.find_element(*TestLocators.EMAIL_INPUT_LOC)
        password = driver.find_element(*TestLocators.PASSWORD_INPUT_LOC)

        name.click()
        name.clear()
        name.send_keys('Anya')

        email.click()
        email.clear()
        email.send_keys('peleeva555555@gmail.com')

        password.click()
        password.clear()
        password.send_keys('pew123!')

        driver.find_element(*TestLocators.SIGN_UP_CONFIRMATION_LOC).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.LOG_IN_PAGE_URL))
