from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

email_path = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')
password_path = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input')

email_path.clear()
password_path.clear()

email_path.send_keys('peleeva5@gmail.com')
password_path.send_keys('pew123!')

log_in = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button')
log_in.click()

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()

try:
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/div/div/main/section[1]/h1'),
                                                          'Соберите бургер'))
    print('Переход в Конструктор выполнен успешно')
except TimeoutException:
    print('Переход в Конструктор не выполнен успешно')

driver.quit()