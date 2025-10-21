import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_001.py",
    "tests/test_002.py",
    "tests/test_003.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)