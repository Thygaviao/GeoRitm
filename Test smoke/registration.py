from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print('Версия теста 1.0, для прохождения капчи введите её в командную строку, когда тест приостановится.')
usermail = input('Введите ваш E-mail для подтверждения регистрации: ')

link = input('Введите адрес инсталляции GeoRITMы. Не забудьте про порт: ')
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

registration = browser.find_element(By.LINK_TEXT, 'Регистрация').click()
name = browser.find_element(By.NAME, 'fname').send_keys('Test')
lastname = browser.find_element(By.NAME, 'sname').send_keys('NeTest')
mail = browser.find_element(By.NAME, 'email').send_keys(usermail)
phone = browser.find_element(By.NAME, 'phone').send_keys('89999999999')
company = browser.find_element(By.NAME, 'company').send_keys('Рога и копыта')
password = browser.find_element(By.XPATH, '//*[@id="auth"]/div[2]/form/div[2]/div[6]/input')
password.send_keys('12345678')
passwordRepeat = browser.find_element(By.XPATH, '//*[@id="auth"]/div[2]/form/div[2]/div[7]/input')
passwordRepeat.send_keys('12345678')
company = browser.find_element(By.NAME, 'secret').send_keys('ПукСренькЯРобот')
captcha = input('Введите капчу СЮДА: ')
captcha_answer = browser.find_element(By.XPATH, '//*[@id="auth"]/div[2]/form/div[2]/div[9]/input').send_keys(captcha)
browser.find_element(By.NAME, 'acceptUA').click()
browser.find_element(By.XPATH, '//*[@id="auth"]/div[2]/form/div[3]/button').click()
time.sleep(10)
browser.quit()
