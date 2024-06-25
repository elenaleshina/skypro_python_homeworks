from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get(" http://uitestingplayground.com/textinput")
    button_name = driver.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = driver.find_element("By.ID", "id_of_element").click()
    print(driver.find_element("By.ID", "id_of_element").text)


except Exception as ex:
    print(ex)
finally:
    driver.quit()