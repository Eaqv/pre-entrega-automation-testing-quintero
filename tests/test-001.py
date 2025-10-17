import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.helpers import esperar_elemento

def test_login_exitoso():
    print("Test inciado")
    service = Service(r"C:\ruta\a\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    # ... completar lógica de login
    driver.quit()