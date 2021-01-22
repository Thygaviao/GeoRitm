from selenium import webdriver
from selenium.webdriver.common.by import By


def test_main_page():

    welcome_example = 'Добро пожаловать в GeoRitm!'
    p_welcome_example = 'Контролируйте свою недвижимость и мобильные объекты с помощью облачного сервиса GeoRitm.'
    vygody_example = 'Ваши выгоды и возможности с GeoRitm'
    GRmob_example = 'GeoRitm для мобильных устройств'
    GRmob_opisanie_example = 'Установите официальное приложение GeoRitm и сохраняйте контроль, где бы Вы ни находились.'

    link = "http://10.78.15.5:8080/"

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)

    welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/h2[1]').text
    if welcome == welcome_example:
        print('Надпись "Добро пожаловать..." соответствует ожиданиям')
    else:
        print('Надпись "Добро пожаловать..." сломалась')

    p_welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[1]').text
    if p_welcome == p_welcome_example:
        print('Подзаголовок "Контролируйте свою недвижимость..." соответствует ожиданиям')
    else:
        print('Подзаголовок сломался')

    vygody = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[2]/a').text
    if vygody == vygody_example:
        print('Надпись "Ваши выгоды и ..." соответствует ожиданиям')
    else:
        print('Надпись "Ваши выгоды и ..." сломалась')

    GRmob = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/h2[2]').text
    if GRmob == GRmob_example:
        print('Надпись о GR мобильном соответствует ожиданиям')
    else:
        print('Надпись о GR мобильном сломалась')

    GRmob_opisanie = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[3]').text
    if GRmob_opisanie == GRmob_opisanie_example:
        print('Надпись "Установите официальное приложение..." соответствует ожиданиям')
    else:
        print('Надпись "Установите официальное приложение..." сломалась')

    browser.quit()

test_main_page()
