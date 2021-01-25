from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_page():
    print('Тест итальянского языка 1.0')
    welcome_example = 'Benvenuti in GeoRitm!'
    p_welcome_example = 'Controlla il tuo immobile e gli oggetti mobili utilizzando il servizio GeoRitm basato su cloud.'
    vygody_example = 'I vantaggi e le opportunità con il servizio GeoRitm'
    GRmob_example = 'GeoRitm per dispositivi mobili'
    GRmob_opisanie_example = "Installare l'applicazione ufficiale GeoRitm e mantenere il controllo ovunque si trovi."
    authorization_example = 'Autorizzazione'
    username_example = 'Nome utente'
    password_example = 'Password'
    sign_in_example = 'Accedi'
    registration_example = 'Registrazione'
    vosst_parol_example = 'Il recupero della password'


    link = "http://10.78.15.5:8080/"

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)

    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/a').click()
    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/ul/li[3]/a').click()

    welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[3]/h2[1]').text
    if welcome == welcome_example:
        print(f'Надпись "{welcome_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{welcome_example}" сломалась и вместо неё выводится "{welcome}"')

    p_welcome = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[3]/p[1]').text
    if p_welcome == p_welcome_example:
        print(f'Надпись "{p_welcome_example}" соответствует ожиданиям')
    else:
        print(f'Надпсь "{p_welcome_example}" сломалась и вместо неё выводится "{p_welcome}"')

    vygody = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[3]/p[2]/a').text
    if vygody == vygody_example:
        print(f'Надпись "{vygody_example}" соответствует ожиданиям')
    else:
        print(f'Надпись "{vygody_example}" сломалась и вместо неё выводится "{vygody}"')

    GRmob = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[3]/h2[2]').text
    if GRmob == GRmob_example:
        print(f'Надпись "{GRmob_example}" ожиданиям')
    else:
        print(f'Надпись "{GRmob_example}" сломалась и вместо неё выводится "{GRmob}"')

    GRmob_opisanie = browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[2]/div[3]/p[3]').text
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
