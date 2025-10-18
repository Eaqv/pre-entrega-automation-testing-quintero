import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_verificacion_catalogo():
    print("Test catálogo iniciado")
    service = Service(r"C:/Users/Alejandro/Documents/chromedriver-win64/chromedriver.exe")  
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)

    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Vemos si efectivamente se llama Products la pagina

    title_element = driver.find_element(By.CLASS_NAME, "title")
    assert title_element.text == "Products"
    print("El titulo de la pagina es: ",title_element.text)

    # Contamos los productos para ver si hay uno o mas
    
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    print("Vemos ",len(productos), " productos.")

    # Nombre y precio del primer producto
    
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print("1er Producto")
    print(f"Producto: {nombre} - Precio: {precio}")
    

    # Vemos si el menú hamburguesa y el filtro estan presentes
    
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed()
    assert filtro.is_displayed()
    print("Verificamos que esta el menu hamburguesa y el filtro")

    driver.quit()