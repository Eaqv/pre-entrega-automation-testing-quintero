# Proyecto de Automatización

Este proyecto forma parte del curso de Automatizacion QA.
Fue desarrollado utilizando Python, Selenium y Pytest para validar funcionalidades clave del sitio saucedemo.com


## Estructura del Proyecto

    pre-entrega-automation-testing-quintero/
    ├── conftest.py        # Fixture login_in_driver con setup y teardown del navegador
    ├── utils.py           # Función login(driver) usada en el fixture
    ├── runtests.py        # Script para ejecutar todas las pruebas y generar reporte HTML
    │
    ├── tests/
    │   ├── test_001.py    # Prueba de login exitoso
    │   ├── test_002.py    # Verificación del catálogo
    │   └── test_003.py    # Agregar producto al carrito
    │
    ├── report.html        # Reporte generado automáticamente después de correr runtests.py
    ├── requirements.txt   # Dependencias del proyecto
    └── README.md          # Este archivo


## Instalación y Configuración

### Activar el entorno virtual

    .venv\Scripts\activate   # En Windows

### Instalar dependencias

    pip install -r requirements.txt

### Ejecutar todas las pruebas y generar el reporte HTML

    python runtests.py

### Visualizar los resultados

Abrí el archivo report.html en tu navegador.


## Descripción de las Pruebas

**test_001.py** ->	Verifica que el login sea exitoso y que se redirija correctamente al catálogo.

**test_002.py** ->	Valida que el catálogo muestre productos, el título correcto y elementos clave como menú y filtro.

**test_003.py** ->	Agrega un producto al carrito, verifica el contador y confirma que el producto esté presente en el carrito.


## Tecnologías utilizadas

- Python 3.13

- Selenium WebDriver

- Pytest

- pytest-html (para generar reportes)


## Notas

-**conftest.py** contiene el fixture login_in_driver, que realiza el login automáticamente antes de cada prueba.

-**utils.py** incluye la función login(driver), utilizada dentro del fixture.

-**runtests.py** permite ejecutar todas las pruebas y generar el reporte HTML con los resultados.



## Autor

### Edgar Alejandro Quintero Vivas
### edgarquintero00@gmail.com
### DNI: 19.104.682
### Lanús, Argentina
### Proyecto — Curso de Testing Automatizado