import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_login_exitoso():
    print("Test iniciado")
    service = Service(r"C:/Users/Alejandro/Documents/chromedriver-win64/chromedriver.exe")  # ← Asegurate de poner la ruta correcta
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    # Lógica de login básica
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificamos que el login fue exitoso
    assert "inventory.html" in driver.current_url

    driver.quit()