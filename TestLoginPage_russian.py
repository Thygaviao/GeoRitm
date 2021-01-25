from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_page():

    welcome_example = 'Добро пожаловать в GeoRitm!'
    p_welcome_example = 'Контролируйте свою недвижимость и мобильные объекты с помощью облачного сервиса GeoRitm.'
    vygody_example = 'Ваши выгоды и возможности с GeoRitm'
    GRmob_example = 'GeoRitm для мобильных устройств'
    GRmob_opisanie_example = 'Установите официальное приложение GeoRitm и сохраняйте контроль, где бы Вы ни находились.'
    authorization_example = 'Авторизация'
    username_example = 'Имя пользователя'
    password_example = 'Пароль'
    sign_in_example = 'Войти'
    registration_example = 'Регистрация'
    vosst_parol_example = 'Восстановление пароля'


    link = "http://10.78.15.5:8080/"

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)

    welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/h2[1]').text
    if welcome == welcome_example:
        print(f'Надпись "{welcome_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{welcome_example}" сломалась и вместо неё выводится "{welcome}"')

    p_welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[1]').text
    if p_welcome == p_welcome_example:
        print(f'Надпись "{p_welcome_example}" соответствует ожиданиям')
    else:
        print(f'Надпсь "{p_welcome_example}" сломалась и вместо неё выводится "{p_welcome}"')

    vygody = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[2]/a').text
    if vygody == vygody_example:
        print(f'Надпись "{vygody_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{vygody_example}" сломалась и вместо неё выводится "{vygody}"')

    GRmob = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/h2[2]').text
    if GRmob == GRmob_example:
        print(f'Надпись "{GRmob_example}" ожиданиям')
    else:
        print(f'Надпись "{GRmob_example}" сломалась и вместо неё выводится "{GRmob}"')

    GRmob_opisanie = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[1]/p[3]').text
    if GRmob_opisanie == GRmob_opisanie_example:
        print(f'Надпись "{GRmob_opisanie_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{GRmob_opisanie_example}" сломалась и вместо неё выводится "{GRmob_opisanie}"')

    authorization = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[1]/h2').text
    if authorization == authorization_example:
        print(f'Надпись "{authorization_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{authorization_example}" сломалась и вместо нее выводится "{authorization}"')


    username = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[2]/div[1]/label').text
    if username == username_example:
        print(f'Надпись "{username_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{username_example}" сломалась и вместо нее выводится "{username}"')

    password = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[2]/div[2]/label').text
    if password == password_example:
        print(f'Надпись "{password_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{password_example}" сломалась и вместо неё выводится "{password}"')

    sign_in = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/button').text
    if sign_in == sign_in_example:
        print(f'Надпись на кнопке "{sign_in_example}" соответствует ожиданиям')
    else:
        print(f'Надпись на кнопке "{sign_in_example}" сломалась и вместо неё выводится "{sign_in}"')

    vosst_parol = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/a[1]').text
    if vosst_parol == vosst_parol_example:
        print(f'Надпись "{vosst_parol_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{vosst_parol_example}" сломалась и вместо неё выводится "{vosst_parol}"')

    registration = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/a[2]').text
    if registration == registration_example:
        print(f'Надпись "{registration_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{registration_example}" сломалась и вместо неё выводится "{registration}"')

    browser.quit()
