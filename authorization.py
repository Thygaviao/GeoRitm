from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_authorization():
    print('Версия теста 1.0. Когда-нибудь и на PageObject перейдём...')

    link = "http://10.78.15.5:8080/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)

    browser.find_element(By.NAME, 'login').send_keys('root')
    browser.find_element(By.NAME, 'password').send_keys('password')
    browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/button').click()

    time.sleep(10)
    browser.quit()

