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

        assert 'Соберите бургер' in driver.find_element(*TestLocators.CREATE_A_BURGER_LOC).text

    @pytest.mark.usefixtures('driver')
    def test_constructor_categories(self, driver):

        driver.get(TestUrlConstants.MAIN_PAGE_URL)

        pastry = driver.find_element(*TestLocators.PASTRY_LOC)
        souces = driver.find_element(*TestLocators.SOUCES_LOC)
        fillings = driver.find_element(*TestLocators.FILLINGS_LOC)

        souces.click()

        assert 'Соусы' in driver.find_element(*TestLocators.CURRENT_TAB_LOC).text

        fillings.click()

        assert 'Начинки' in driver.find_element(*TestLocators.CURRENT_TAB_LOC).text

        pastry.click()

        assert 'Булки' in driver.find_element(*TestLocators.CURRENT_TAB_LOC).text
