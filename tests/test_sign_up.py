from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

name_path = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')
email_path = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input')
password_path = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/div/input')

name_path.clear()
email_path.clear()
password_path.clear()

name_path.send_keys('Anya')
email_path.send_keys('peleeva5555@gmail.com')
password_path.send_keys('123')

sign_up_confirmation = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button')
sign_up_confirmation.click()

if driver.find_elements(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]"):
        print('Некорректный пароль. Минимальный пароль — шесть символов')

try:
    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/login'))
    print('Регистрация прошла успешно')
except TimeoutException:
    print('Такой пользователь уже существует')

driver.quit()