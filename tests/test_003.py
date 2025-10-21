from selenium.webdriver.common.by import By

def test_agregar_producto_al_carrito(login_in_driver):
    try:
        driver = login_in_driver
        print("Test carrito iniciado")

        # Agregamos el primer producto al carrito
        producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
        nombre_producto = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        producto.find_element(By.TAG_NAME, "button").click()
        print("Seleccionamos:", nombre_producto)

        # Verificamos que el contador del carrito aumentó a 1
        contador = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span")
        assert contador.text == "1", "El contador del carrito no muestra 1"
        print("Carrito =", contador.text)

        # Entramos al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Entramos al carrito")

        # Verificamos que el producto en el carrito coincide
        producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert producto_carrito == nombre_producto, "El producto en el carrito no coincide"
        print("¡Coinciden correctamente!")

    except Exception as e:
        print(f"Error en test_agregar_producto_al_carrito: {e}")
        raise
    finally:
        driver.quit()