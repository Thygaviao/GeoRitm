from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print('Версия теста 1.0. Когда-нибудь и на PageObject перейдём...')

link = input('Введите адрес инсталляции GeoRITM. Не забудьте про порт: ')
browser = webdriver.Chrome()
browser.implicitly_wait(15)
browser.get(link)

browser.find_element(By.NAME, 'login').send_keys('thygaviao@yandex.ru')
browser.find_element(By.NAME, 'password').send_keys('12345678')
browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/div/button').click()

time.sleep(10)
browser.quit()

