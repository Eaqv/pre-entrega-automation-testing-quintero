from selenium.webdriver.common.by import By

def test_inventory_verificado(login_in_driver):
    try:
        driver = login_in_driver

        # Validamos título de la página
        assert driver.title == "Swag Labs", "El título de la página no es correcto"

        # Validamos que el título visual sea 'Products'
        title_element = driver.find_element(By.CLASS_NAME, "title")
        assert title_element.text == "Products", "El encabezado visual no es 'Products'"
        print("Título visual:", title_element.text)

        # Verificamos que haya productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No hay productos visibles en la página"
        print("Cantidad de productos:", len(productos))

        # Mostramos nombre y precio del primero
        nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Primer producto: {nombre} - Precio: {precio}")

        # Verificamos menú hamburguesa y filtro
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert menu.is_displayed(), "El menú hamburguesa no está visible"
        assert filtro.is_displayed(), "El filtro de productos no está visible"
        print("Menú y filtro verificados correctamente")

    except Exception as e:
        print(f"Error en test_inventory_verificado: {e}")
        raise
    finally:
        driver.quit()