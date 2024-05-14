import os
import pytest

def run_tests():
    # Define la ruta de la carpeta donde se encuentran las pruebas
    tests_folder = os.path.abspath("Demo")

    # Configura las opciones de pytest, como generar un reporte en formato junitxml
    # que puede ser utilizado para generar reportes HTML con herramientas como pytest-html.
    options = [
        tests_folder,
        "--html=report.html",  # Generar un reporte html
        "-v"  # Verboso, para mostrar información detallada sobre las pruebas
    ]

    # Ejecuta las pruebas utilizando pytest y las opciones configuradas.
    pytest.main(options)

if __name__ == "__main__":
    run_tests()