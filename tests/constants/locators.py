from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocators:
    LOG_IN_ACCOUNT_LOC = By.XPATH, '//*[contains(@class, "button_size_large")]'
    PERSONAL_ACCOUNT_LOC = By.XPATH, '//*[contains(@class, "AppHeader_header__linkText") and text()="Личный Кабинет"]'
    CONSTRUCTOR_LOC = By.XPATH, '//*[contains(@class, "AppHeader_header__linkText") and text()="Конструктор"]'

    LOG_IN_LOC = By.XPATH, '//*[contains(@class, "button_size_medium")]'
    SIGN_UP_CONFIRMATION_LOC = By.XPATH, '//*[contains(@class, "button_size_medium") and text()="Зарегистрироваться"]'
    LOG_OUT_LOC = By.XPATH, '//*[contains(@class, "Account_button") and text()="Выход"]'

    SIGN_UP_FORGOT_PASSWORD_AUTH_LOC = By.XPATH, '//*[contains(@class, "Auth_link")]'

    SIGN_UP_FROM_LOG_IN_PAGE_LOC = By.XPATH, '//*[contains(@class, "Auth_link") and text()="Зарегистрироваться"]'

    PASTRY_LOC = By.XPATH, '//*[contains(@class, "text_type_main-default") and text()="Булки"]'
    SOUCES_LOC = By.XPATH, '//*[contains(@class, "text_type_main-default") and text()="Соусы"]'
    FILLINGS_LOC = By.XPATH, '//*[contains(@class, "text_type_main-default") and text()="Начинки"]'

    EMAIL_INPUT_LOC = By.XPATH, '//*[contains(@class, "input__placeholder text noselect text_type_main-default") and text()="Email"]/following-sibling::*[1]'
    PASSWORD_INPUT_LOC = By.XPATH, '//*[contains(@class, "input__placeholder text noselect text_type_main-default") and text()="Пароль"]/following-sibling::*[1]'
    NAME_INPUT_LOC = By.XPATH, '//*[contains(@class, "input__placeholder text noselect text_type_main-default") and text()="Имя"]/following-sibling::*[1]'

    INCORRECT_PASSWORD_MSG_LOC = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'