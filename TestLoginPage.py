from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import TestLoginPage_russian as test_ru
import TestLoginPage_english as test_en
import TestLoginPage_italiano as test_it
import TestLoginPage_deutsch as test_de

test_ru.test_login_page()
test_en.test_login_page()
test_it.test_login_page()
test_de.test_login_page()




