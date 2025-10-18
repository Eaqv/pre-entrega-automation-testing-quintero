import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_agregar_producto_al_carrito():
    print("Test carrito iniciado")
    service = Service(r"C:/Users/Alejandro/Documents/chromedriver-win64/chromedriver.exe") 
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)

    # Paso 1: Login
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Nos logueamos")
    
    # Agregamos el primer producto al carrito
    
    producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre_producto = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    producto.find_element(By.TAG_NAME, "button").click()
    print("Seleccionamos: ",nombre_producto)

    # Vemos si el contador del carrito aumento a 1
    
    contador = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span")
    assert contador.text == "1"
    print("Carrito = ",contador.text)

    # Vamos al carrito
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("Entramos al carrito")
    
    # Vemos si esta el producto anteriormente seleccionado

    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto
    print("Si coinciden!")

    driver.quit()