from selenium import webdriver
from selenium.webdriver.common.by import By
import test_localization_map_ru as test_ru
import test_localization_map_en as test_en
import test_localization_map_it as test_it
import test_localization_map_de as test_de

test_ru.test_localization_map()
test_en.test_localization_map()
test_it.test_localization_map()
test_de.test_localization_map()