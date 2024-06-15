from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/classattr")
#запускаем скрипт 3 раза
    for _ in range(3):
#кликаем синюю кнопку 3 раза
     blue_button = driver.find_element()
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]
    blue_button.click()

    driver = webdriver.Firefox()
try:
    driver.get("http://uitestingplayground.com/classattr")
#запускаем скрипт 3 раза
    for _ in range(3):
#кликаем синюю кнопку 3 раза
     blue_button = driver.find_element()
    "xpath", '//batton[contains(concat("", normalize-space(@class)], ''). 'btn-primary')
    blue_button.click()
    sleep(2)
#кликyть на ок в модальном окне
    driver.switch_to.alert.accept()

except Exception as ex:
    print(ex)
finally:
    driver.quit()    
