from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_ul_localization():
    link = "http://10.78.15.5:8080/"

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)
    actionChains = ActionChains(browser)

    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/a').click()
    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/ul/li[4]/a').click()
    browser.find_element(By.NAME, 'login').send_keys('root')
    browser.find_element(By.NAME, 'password').send_keys('password')
    browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/button').click()


    maps_example = ['Karte Yandex', 'Satellit Yandex', 'Hybrid Yandex', 'Karte Google',
        'Satellit Google', 'Hybrid Google', 'Relief Google', 'Karte OpenStreetMap', 'Fahrzeug OpenStreetMap']
    address = ['Adresse', 'Objekte', 'EinsatzGr']
    profile = ['Verwaltung', 'Passwort ändern', 'Über das System', 'Abmelden']
    objects = ['Mobile Objekte', 'Stationäre Objekte']
    plus_objects = ['Objekt hinzufügen', 'Gruppe hinzufügen']
    ul_objects_mobile = ['Track aufbauen', 'Bericht aufbauen',
                         'Verfolgung aktivieren', 'Karte des Objekts öffnen', 'Ereignisse und Journal']
    ul_objects_group = ['Bericht zur Gruppe aufbauen', 'Gruppe umbenennen',
                        'Objekt hinzufügen', 'Untergruppe hinzufügen']

    i = 0
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/a').click()
    for name in maps_example:
        i += 1
        list = browser.find_element(By.XPATH,'//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/ul/li['+str(i)+']')
        list = list.text
        if name != list:
            print(f'Перевод карты "{name}" сломался (или список карт изменился), теперь выводится "{list}"')

    i = 0
    browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/form/div/a').click()
    for name in address:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[1]/form/div/ul/li['+str(i)+']')
        list = list.text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    i = 0
    browser.find_element(By.XPATH, '//*[@id="account-nav"]/li[3]/a').click()
    for name in profile:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="account-nav"]/li[3]/ul/li['+str(i)+']').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    i = 0
    browser.find_element(By.XPATH, '//*[@id="objects-tree"]/div[1]/div/a').click()
    for name in objects:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="objects-tree"]/div[1]/div/ul/li['+str(i)+']').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    i = 0
    browser.find_element(By.XPATH, '//*[@id="mobile"]/div[1]/div[2]/a/i').click()
    for name in plus_objects:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="mobile"]/div[1]/div[2]/ul/li[' + str(i) + ']/a').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    browser.find_element(By.XPATH, '//*[@id="mobile"]/div[1]/div[2]/a/i').click()
    i = 0
    element = browser.find_element(By.XPATH, '//*[@id="stat-tree"]/div[5]/div/div[2]/div[2]')
    actionChains.context_click(element).perform()
    for name in ul_objects_group:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="ui-id-5"]/li['+str(i)+']/a').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    i = 0
    browser.find_element(By.XPATH, '//*[@id="mobile-tree"]/div[5]/div/div[2]/div[1]/div/i[1]').click()
    element = browser.find_element(By.XPATH, '//*[@id="stat-tree"]/div[5]/div/div[3]')
    actionChains.context_click(element).perform()
    for name in ul_objects_mobile:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="ui-id-5"]/li[' + str(i) + ']/a').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')
    browser.quit()


def test_buildings_ul():
    link = "http://10.78.15.5:8080/"

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)
    actionChains = ActionChains(browser)

    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/a').click()
    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/ul/li[4]/a').click()
    browser.find_element(By.NAME, 'login').send_keys('root')
    browser.find_element(By.NAME, 'password').send_keys('password')
    browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/button').click()

    ul_objects_buildings = ['Bericht aufbauen', 'Karte des Objekts öffnen',
                            'Koordinaten des Objekts ändern', 'Ereignisse und Journal']
    ul_objects_group = ['Bericht zur Gruppe aufbauen', 'Gruppe umbenennen',
                        'Objekt hinzufügen', 'Untergruppe hinzufügen']
    i = 0


    browser.find_element(By.XPATH, '//*[@id="objects-tree"]/div[1]/div/a').click()
    browser.find_element(By.XPATH, '//*[@id="objects-tree"]/div[1]/div/ul/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="stat-tree"]/div[5]/div/div[2]/div[1]/div/i[1]').click()
    element = browser.find_element(By.XPATH, '//*[@id="stat-tree"]/div[5]/div/div[4]/div[2]')
    actionChains.context_click(element).perform()
    for name in ul_objects_buildings:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="ui-id-6"]/li['+str(i)+']/a').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')

    i = 0
    element = browser.find_element(By.XPATH, '//*[@id="stat-tree"]/div[5]/div/div[2]/div[2]')
    actionChains.context_click(element).perform()
    for name in ul_objects_group:
        i += 1
        list = browser.find_element(By.XPATH, '//*[@id="ui-id-6"]/li['+str(i)+']').text
        if list != name:
            print(f'Список сломался и вместо "{name}" выводится "{list}"')
    browser.quit()
