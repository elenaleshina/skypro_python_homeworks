from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
try:
    сount = 0
    driver.get("http://uitestingplayground.com/dynamicid")
 #кликаем синюю кнопку
    blue_button = driver.find_element(
        "xpath", '//batton[text() = "Batton with Dynamic ID"]'). click()
driver = webdriver.Firefox()
try:
    сount = 0
    driver.get("http://uitestingplayground.com/dynamicid")
#кликаем синюю кнопку
    blue_button = driver.find_element(
        "xpath", '//batton[text() = "Batton with Dynamic ID"]'). click()
#кликаем синюю кнопку 3 раза
for _ in range(3):
    blue_button = driver.find_element(
        "xpath", '//batton[text() = "Batton with Dynamic ID"]'). click()
    сount = сount +1
    sleep(2)
    print(сount)
except Exception as ex:
    print(ex)
finally:
    driver.quit()