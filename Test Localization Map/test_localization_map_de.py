from selenium import webdriver
from selenium.webdriver.common.by import By


def test_localization_map():
    link = "http://10.78.15.5:8080/"
    mashtab_example = '1 km'
    ritm_nadpis_example = "Entwickler und Hersteller des Systems: Firma Ritm"
    print_map_example = 'Karte drucken'
    selfscaling_example = 'Automatischer Maßstab'
    minus_example = 'Verkleinern'
    plus_example = 'Vergrößern'
    down_example = 'Runter'
    left_example = 'Nach links'
    right_example = 'Nach rechts'
    up_example = 'Hoch'
    traffic_example = 'Staus'
    ruler_example = 'Lineal'
    clean_map_example = 'Inhalt der Karte löschen'

    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/a').click()
    browser.find_element(By.XPATH, '//*[@id="lang-nav"]/li/ul/li[4]/a').click()
    browser.find_element(By.NAME, 'login').send_keys('root')
    browser.find_element(By.NAME, 'password').send_keys('password')
    browser.find_element(By.XPATH, '//*[@id="auth"]/div/div/div[1]/form/div[3]/button').click()

    mashtab = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div').text
    if mashtab != mashtab_example:
        print(f'Неверный перевод, ожидалось: {mashtab_example}, а получилось {mashtab}')

    ritm_nadpis = browser.find_element(By.XPATH, '//*[@id="company-info"]/a').text
    if ritm_nadpis != ritm_nadpis_example:
        print(f'Неверный перевод, ожидалось: {ritm_nadpis_example}, а получилось {ritm_nadpis}')

    print_map = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/button[2]')
    print_map = print_map.get_attribute('title')
    if print_map != print_map_example:
        print(f'Неверный перевод, ожидалось: {print_map_example}, а получилось {print_map}')

    selfscaling = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/button[1]')
    selfscaling = selfscaling.get_attribute('title')
    if selfscaling != selfscaling_example:
        print(f'Неверный перевод, ожидалось: {selfscaling_example}, а получилось {selfscaling}')

    minus = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]')
    minus = minus.get_attribute('title')
    if minus != minus_example:
        print(f'Неверный перевод, ожидалось: {minus_example}, а получилось {minus}')

    plus = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]')
    plus = plus.get_attribute('title')
    if plus != plus_example:
        print(f'Неверный перевод, ожидалось: {plus_example}, а получилось {plus}')

    down = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[4]/a')
    down = down.get_attribute('title')
    if down != down_example:
        print(f'Неверный перевод, ожидалось: {down_example}, а получилось {down}')

    left = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/a')
    left = left.get_attribute('title')
    if left != left_example:
        print(f'Неверный перевод, ожидалось: {left_example}, а получилось {left}')

    up = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a')
    up = up.get_attribute('title')
    if up != up_example:
        print(f'Неверный перевод, ожидалось: {up_example}, а получилось {up}')

    right = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/a')
    right = right.get_attribute('title')
    if right != right_example:
        print(f'Неверный перевод, ожидалось: {ruler_example}, а получилось {right}')

    traffic = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]').text
    if traffic != traffic_example:
        print(f'Неверный перевод, ожидалось: {traffic_example}, а получилось {traffic}')

    ruler = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div')
    ruler = ruler.get_attribute('title')
    if ruler != ruler_example:
        print(f'Неверный перевод, ожидалось: {ruler_example}, а получилось {ruler}')

    clean_map = browser.find_element(By.XPATH, '//*[@id="page"]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/button[2]')
    clean_map = clean_map.get_attribute('title')
    if clean_map != clean_map_example:
        print(f'Неверный перевод, ожидалось: {clean_map_example}, а получилось {clean_map}')

    browser.quit()
