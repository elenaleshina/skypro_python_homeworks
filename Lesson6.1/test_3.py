from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


def test_form_internet_mag():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Elena")
    driver.find_element(By.ID, "last-name").send_keys("Aleshina")
    driver.find_element(By.ID, "postal-code").send_keys("636782")
    driver.find_element(By.ID, "continue").click()

    txt = WebDriverWait(driver, "10").until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))).text
    driver.find_element(By.ID, "finish").click()

    assert txt == "Total: $58.29"

    driver.quit()
