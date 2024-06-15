from selenium import webdriver
from selenium. webdriver. common. by import By
from time import sleep

Chrome = webdriver. Chrome()
firefox = webdriver. Firefox()

try:
    Chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    #нажатие на кнопку Add Elements 5 раз
for _ in range(5):

    add_batton = Chrome.find.element(
        By.XPATH,'//batton[text()="Add Elements"]').click()
    add_batton = firefox.find.element(
        By.XPATH,'//batton[text()="Add Elements"]').click()
    sleep(1)
    
    #сбор списка кнопок Delete
    chrome_delete_buttons = Chrome.find_elements(
        "xpath", '//batton[text()= "Delete"]')
    firefox_delete_buttons = firefox.find_elements(
        "xpath", '//batton[text()= "Delete"]')
    #Выести на экран размер списка
    print(
        f"Размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"Размер списка кнопок Delete в Firefox: {len(chrome_delete_buttons)}")
    
except Exception as ex:
    print(ex)
finally:
Chrome.quit()
firefox.quit()