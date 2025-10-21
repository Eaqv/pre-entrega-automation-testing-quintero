import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import login  # 👈 Importás la función

@pytest.fixture
def login_in_driver():
    service = Service(r"C:/Users/Alejandro/Documents/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    login(driver)  # 👈 Usás la función del utils

    yield driver
    driver.quit()