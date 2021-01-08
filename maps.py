from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_move_map():
    # Начинаем проверять карту
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]').click()
    time.sleep(1)
    # Кнопка увеличения масштаба
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]').click()
    # Кнопка уменьшения масштаба
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/button[1]').click()
    time.sleep(1)
    # автомасштабирование
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[4]/a').click()
    time.sleep(1)
    # Перемещение карты вниз
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a').click()
    time.sleep(1)
    # Перемещение карты вверх
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/a').click()
    time.sleep(1)
    # Перемещение карты влево
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/a').click()
    time.sleep(1)
    # Перемещение карты вправо
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]').click()


print('Версия теста 1.0. Когда-нибудь PyTest подключим.')
link = input('Введите адрес инсталляции GeoRITM. Не забудьте про порт: ')

browser = webdriver.Chrome()
browser.implicitly_wait(15)
browser.get(link)

browser.find_element(By.NAME, 'login').send_keys('thygaviao@yandex.ru')
browser.find_element(By.NAME, 'password').send_keys('12345678')
browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/div/button').click()
test_move_map()

browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[2]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[3]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[4]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[5]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[6]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[7]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[8]').click()
test_move_map()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div').click()
browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li[9]').click()
test_move_map()
browser.quit()



