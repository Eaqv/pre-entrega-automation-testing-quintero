from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
    driver = login_in_driver

    try:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        print("Login exitoso y validado correctamente")
    except AssertionError as e:
        try:
            error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            print(f"Error detectado en pantalla: {error_msg}")
        except:
            print("No se redirigió correctamente y no se encontró mensaje de error")
        raise e