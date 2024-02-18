from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/')

pastry = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span')
souces = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span')
fillings = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span')

souces.click()
try:
    WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[2]'),
                                                              'Соус'))
except TimeoutException:
    print('Не удалось переключить категорию')

fillings.click()
try:
    WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/div/div/main/section[1]/div[2]'),
                                                              'Мясо'))
except TimeoutException:
    print('Не удалось переключить категорию')

pastry.click()
try:
    WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[1]'),
                                                              'булка'))
except TimeoutException:
    print('Не удалось переключить категорию')

driver.quit()
