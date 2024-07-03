import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestFlujoHL5():
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        if os.name == 'nt':  # Si el sistema operativo es Windows
            chromedriver_path = "C:\\chromedriver-win64\\chromedriver.exe"
        else:  # Si el sistema operativo es Linux (GitHub Actions)
            chromedriver_path = "/usr/bin/chromedriver"

        chrome_service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_flujo_HL_5(self):
        # Test name: flujo 5

        # Parte cero: reinicio de cliente

        # 1 | Abre el formulario de reinicio de cliente
        self.driver.get('https://4er2v88hf6.execute-api.us-east-1.amazonaws.com/pwa-reset-test-deals')
        # 2 | Pone el navegador en pantalla completa
        self.driver.maximize_window()
        # 3 | Hace una espera de 5 segundos
        time.sleep(5)

        # Reinciar cliente 1
        # 4 | Selecciona el listbox
        select = Select(self.driver.find_element(By.ID, "elementos"))
        # 5 | Selecciona una opción del listbox según el index
        # index 17 = PruebaCliente 1
        # index 18 = PruebaCliente 2
        # index 19 = PruebaCliente 3
        # index 20 = PruebaCliente 4
        select.select_by_index(17)
        # 6 | Selecciona el check list de reinicio de plan de pago
        # Reiniciar formulario de cliente = .radio-label:nth-child(1) span
        # Reiniciar plan de pago = .radio-label:nth-child(3) span
        # Reiniciar tod0 = .radio-label:nth-child(5) span
        self.driver.find_element(By.CSS_SELECTOR, ".radio-label:nth-child(3) span").click()
        # 7 | Preciosa el botón de enviar para realizar la acción
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        # 8 | Hace una espera de 5 segundos
        time.sleep(5)
        # 9 | Espera que aparezca la alerta del navegador
        alert = self.driver.switch_to.alert
        # 10 | Verifica que la alerta diga "Datos reiniciados correctamente"
        assert alert.text == "Datos reiniciados correctamente"
        # 11 | Acepta la notificación
        alert.accept()

        # Primera parte: Crear plan de pago con modificaciones
        # 1 | Abre el módulo de Asesor de ventas
        self.driver.get("http://concasa-real-estate.s3-website-us-east-1.amazonaws.com/")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Presiona el espacio del email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 4 | Digita el email "usiel.ramirez@concasa.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        # 5 | Presiona el espacio del contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 6 | Digita la contraseña
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | Presiona el botón de inicio de sesión
        self.driver.find_element(By.CSS_SELECTOR, ".section-container:nth-child(6) > .mr-2").click()
        # 8 | Espera que la sección de gestión de ventas este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Gestión de ventas")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Gestión de ventas")))
        # 9 | Presiona la sección de gestión de ventas del menu hamburguesa
        element = self.driver.find_element(By.LINK_TEXT, "Gestión de ventas")
        self.driver.execute_script("arguments[0].click();", element)
        # 10 | Espera que el expediente este disponible
        # .even:nth-child(1) > td:nth-child(1) = Cliente prueba 1
        # .even:nth-child(2) > td:nth-child(1) = Cliente prueba 2
        # .even:nth-child(3) > td:nth-child(1) = Cliente prueba 3
        # .even:nth-child(4) > td:nth-child(1) = Cliente prueba 4
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")))  # el expediente que abrimos
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")))
        # 11 | Presiona el expediente al que se va a crear el plan de pago
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")
        self.driver.execute_script("arguments[0].click();", element1)
        # 12 | Espera que el espacio de cantidad de cuotas este disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".number-input-container")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".number-input-container")))
        # 13 | Limpia el espacio de cantidad de cuotas
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").clear()
        # 14 | Presiona el espacio de cantidad de cuotas
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".number-input-container")
        self.driver.execute_script("arguments[0].click();", element1)
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.BACKSPACE)
        # 15 | Digita la cantidad de cuotas que quiere
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys("15")
        # 16 | Presiona la tecla Enter
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.ENTER)
        # 17 | Espera que el area de notas este disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-area-input-container")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-area-input-container")))
        # 18 | Presiona el espacio de notas
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".text-area-input-container")
        self.driver.execute_script("arguments[0].click();", element1)
        # 19 | Digita la descripción o justificación del plan de pagos con modificación
        self.driver.find_element(By.CSS_SELECTOR, ".text-area-input-container").send_keys("necesidad de más cuotas")
        # 20 | Espera que el botón de enviar aprobación esté disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".send-to-aprove-button")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".send-to-aprove-button")))
        # 21 | Presiona el botón de enviar a aprobación
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".send-to-aprove-button")
        self.driver.execute_script("arguments[0].click();", element1)
        # 22 | Espera que le botón de confirmar esté disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
        # 23 | Presiona el botón de confirmar la creación de plan
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element)

        # segunda parte: rechazar plan de pago por el SAF
        # 1 | Abre el módulo de Asesor financiero
        self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        # 3 | Espera que el espacio de email este cargado y disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, "emaiI")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "emaiI")))
        # 4 | Presiona el espacio del email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 5 | Digita el email
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        # 6 | Presiona el espacio de contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 7 | Digita la contraseña
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 8 | Presiona el botón de iniciar sesión
        self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button").click()
        # 9 | Espera que el botón de aprobaciones este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//li[5]/a")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[5]/a")))
        # 10 | Presiona el botón aprobaciones del menú hamburguesa
        element = self.driver.find_element(By.XPATH, "//li[5]/a")
        self.driver.execute_script("arguments[0].click();", element)
        # 11 | Espera que el expediente que se va a aprobar esté disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "9911")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "9911")))
        # 12 | Presiona el expediente para la aprobación
        element = self.driver.find_element(By.LINK_TEXT, "9911")
        self.driver.execute_script("arguments[0].click();", element)
        # 13 | Espera que el espacio de razón este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "comment")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comment")))
        # 14 | Presiona el espacio de razón
        element = self.driver.find_element(By.ID, "comment")
        self.driver.execute_script("arguments[0].click();", element)
        # 15 | Digita la razón para la aprobación
        self.driver.find_element(By.ID, "comment").send_keys("No es factible")
        # 16 | Presiona el botón de aprobación
        element = self.driver.find_element(By.CSS_SELECTOR, ".reject-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 17 | Espera que el botón "si" para confirmar la aprobación
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/button[2]")))
        # 18 | Presiona el botón si para confirmar la aprobación
        element = self.driver.find_element(By.XPATH, "//div[3]/button[2]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(8)


