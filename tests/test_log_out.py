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

my_account = driver.find_element(By.LINK_TEXT, "Личный Кабинет")
my_account.click()

WebDriverWait(driver, 5).until(
        expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

exit_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")
exit_button.click()

try:
    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/login'))
    print('Выход выполнен успешно')
except TimeoutException:
    print('Выход не выполнен успешно')

driver.quit()