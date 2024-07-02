import pytest
from constants.locators import TestLocators
from constants.constants import TestUrlConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:

    @pytest.mark.usefixtures('driver')
    def test_main_page_to_personal_account(self, driver):

        driver.get(TestUrlConstants.MAIN_PAGE_URL)

        driver.find_element(*TestLocators.LOG_IN_ACCOUNT_LOC).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.LOG_IN_PAGE_URL))

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

        assert WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestUrlConstants.PROFILE_PAGE_URL))




