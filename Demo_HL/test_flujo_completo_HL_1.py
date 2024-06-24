import os

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestflujocompletoHL1():
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

    def test_flujo_completo_HL_1(self):

        # El primer paso del flujo es crear el perfil del cliente.
        # 1 | Abre el módulo de clientes
        self.driver.get("http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Clickea en el espacio de email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 4 | Digita el email "prueba.cliente1.concasahome@yopmail.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("prueba.cliente1.concasahome@yopmail.com")
        # 5 | Clickea en el espacio de contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 6 | Digita la contraseña "123456"
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | Clickea el botón de loggearse
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(10) > .initButtonLogin").click()
        # 8 | Hace una pausa de 15 segundos para esperar que la página cargue
        time.sleep(15)
        # 9 | Presiona el botón de empecemos
        self.driver.find_element(By.XPATH, "//button").click()
        # 10 | Presiona el botón de persona
        self.driver.find_element(By.XPATH, "//button").click()
        # 11 | Presiona tipo de identificación
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        # 12 | Selecciona el tipo de identificación "Nacional"
        self.driver.find_element(By.XPATH, "//section/div/div/div[2]/div/div").click()
        # 13 | Limpia el espacio de número de identificación
        self.driver.find_element(By.ID, "idNumber").clear()
        # 14 | Presiona el espacio de número de identificación
        self.driver.find_element(By.ID, "idNumber").click()
        # 15 | Digita la identificación "117970499"
        self.driver.find_element(By.ID, "idNumber").send_keys("117970499")
        # 16 | Presiona el botón de siguiente
        self.driver.find_element(By.XPATH, "//button").click()
        # 17 | Hace una espera que busque el cliente por númerdo de identificación para que este disponible el botón de siguiente
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button")))
        # 18 | Presiona el botón de siguiente
        self.driver.find_element(By.XPATH, "//button").click()
        # 19 | Presiona el combo box del número celular
        self.driver.find_element(By.XPATH, "//section/div/div/div/div/div").click()
        # 20 | Presiona el número de costa rica "506"
        self.driver.find_element(By.XPATH, "//div[52]/div").click()
        # 21 | Limpia el espacio donde se ingresa el número
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").clear()
        # 22 | Presiona el espacio donde se ingresa el número
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").click()
        # 23 | Digita el número de telefono "1234 5678"
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").send_keys("1234 5678")
        # 24 | Presiona el botón de siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 25 | Presiona el boton de "Territorio contarricense"
        self.driver.find_element(By.XPATH, "//button").click()
        # 26 | Presiona el combo box de "provincia"
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div/div/div/div/div").click()
        # 27 | Selecciona la provincia
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div/div").click()
        # 28 | Presiona el combo box de "cantón"
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/div/div/div").click()
        # 29 | Selecciona el cantón
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div[2]/div/div").click()
        # 30 | Presiona el combo box de "distrito"
        self.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div").click()
        # 31 | Selecciona el  cantón
        self.driver.find_element(By.XPATH, "//div/div[3]/div/div/div/div[2]/div/div").click()
        # 32 | Limpia el espacio de dirección exacta
        self.driver.find_element(By.ID, "exactDirection").clear()
        # 33 | Presiona el espacio de dirección exacta
        self.driver.find_element(By.ID, "exactDirection").click()
        # 34 | Digita la dirección exacta "abcdfg"
        self.driver.find_element(By.ID, "exactDirection").send_keys("abcdfg")
        # 35 | Presionas la tecla enter
        self.driver.find_element(By.ID, "exactDirection").send_keys(Keys.ENTER)
        # 36 | Presionas el botón de siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 37 | Presionas el botón Asalariado
        self.driver.find_element(By.XPATH, "//button").click()
        # 38 | Limpia el espacio del nombre de la empresa
        self.driver.find_element(By.ID, "companyName").clear()
        # 39 | Presiona el espacio de nombre de la empresa
        self.driver.find_element(By.ID, "companyName").click()
        # 40 | Digita el nombre de la empresa "Intel"
        self.driver.find_element(By.ID, "companyName").send_keys("intel")
        # 41 | Limpia el espacio de número de telefono
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").clear()
        # 42 | Limpia el espacio de número de telefono
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").click()
        # 43 | Digita el número de la empresa "8765 4321"
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").send_keys("8765 4321")
        # 44 | Limpia el espacio de dirección
        self.driver.find_element(By.ID, "addressCompany").clear()
        # 45 | Presiona el espacio de dirección
        self.driver.find_element(By.ID, "addressCompany").click()
        # 46 | Digita la dirección
        self.driver.find_element(By.ID, "addressCompany").send_keys("abcdfg")
        # 47 | Presiona el botón de siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 48 | Limpia el espacio de ocupación
        self.driver.find_element(By.ID, "companyName").clear()
        # 49 | Presiona el espació de ocupación
        self.driver.find_element(By.ID, "companyName").click()
        # 50 | Digita la ocupación "Ingeniero"
        self.driver.find_element(By.ID, "companyName").send_keys("ingeniero")
        # 51 | Presiona el combo box de "¿Cuanto tiempo tiene de estar con la empresa?"
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        # 52 | Selecciona la opción años
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div/div").click()
        # 53 | Limpia el espacio de años
        self.driver.find_element(By.ID, "timeCompany").clear()
        # 54 | Presiona el espacio de timpo en la compañia
        self.driver.find_element(By.ID, "timeCompany").click()
        # 55 | Digita la cantidad de años "5"
        self.driver.find_element(By.ID, "timeCompany").send_keys("5")
        # 56 | Presiona la tecla de "Enter"
        self.driver.find_element(By.ID, "timeCompany").send_keys(Keys.ENTER)
        # 57 | Presiona el botón de siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 58 | Selecciona el combo box de seleccionar moneda
        self.driver.find_element(By.CSS_SELECTOR, ".css-g1nrkn").click()
        # 59 | Presiona el tipo de moneda "USD"
        self.driver.find_element(By.XPATH, "//section/div/div/div/div[2]/div/div").click()
        # 60 | Limpia el espacio del monto de salario
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").clear()
        # 61 | Presiona el espacio del monto de salario
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").click()
        # 62 | Digita el monto del salario "5000"
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").send_keys("5,000")
        # 63 | Presiona la tecla "Enter"
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").send_keys(Keys.ENTER)
        # 64 | Presiona el botón de siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 65 | Presiona el botón de "No" si tiene otra fuente de ingreso
        element = self.driver.find_element(By.XPATH, "//button[2]")
        self.driver.execute_script("arguments[0].click();", element)
        # 66 | Presiona el botón de "Si" si tiene deudas personales
        self.driver.find_element(By.XPATH, "//button").click()
        # 67 | Selecciona el combo box de moneda
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        # 68 | Presiona el tipo de moneda "USD"
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div/div").click()
        # 69 | Limpia el espacio de la monto de la deuda
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").clear()
        # 70 | Selecciona el espacio del monto
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").click()
        # 71 | Digita el monto de la deuda "5000"
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").send_keys("5,000")
        # 72 | Presiona le tecla "Enter"
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").send_keys(Keys.ENTER)
        # 73 | Presiona el botón siguiente
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 74 | Presiona el "He leído y acepto los términos y condiciones"
        self.driver.find_element(By.CSS_SELECTOR, "i").click()
        # 75 | Presiona el botón de "Realizar solicitud" | Aquí se termina la creación del perfil del cliente
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex:nth-child(5) > .font-lato").click()
        # Una espera de 5 segundos para que se cree el perfil
        time.sleep(5)


        # El segundo paso del flujo es la creación del plan de pagos del cliente en el módulo de asesor de ventas
        # 1 | Abre el módulo de asesor de ventas
        self.driver.get("http://concasa-real-estate.s3-website-us-east-1.amazonaws.com/")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Hace una espera para que cargue la página
        time.sleep(5)
        # 4 | Presiona el espacio de email
        element = self.driver.find_element(By.NAME, "emaiI")
        self.driver.execute_script("arguments[0].click();", element)
        # 5 | Digita el email "usiel.ramirez@concasa.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        # 6 | Presiona el espacio de contraseña
        element = self.driver.find_element(By.NAME, "passI")
        self.driver.execute_script("arguments[0].click();", element)
        # 7 | Digita la contraseña "123456"
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 8 | Presiona el botón para iniciar sesión
        element = self.driver.find_element(By.CSS_SELECTOR, ".section-container:nth-child(6) > .mr-2")
        self.driver.execute_script("arguments[0].click();", element)
        # Redirección al apartado de gestión de ventas
        # 9 | Hace una espera que el botón de gestión de ventas esté disponible para presionar
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Gestión de ventas")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Gestión de ventas")))
        # 10 | Presiona el botón de gestión de ventas
        element = self.driver.find_element(By.LINK_TEXT, "Gestión de ventas")
        self.driver.execute_script("arguments[0].click();", element)
        # Selección del expediente que vamos a crearle un plan de pagos
        # .even:nth-child(1) > td:nth-child(1) = Cliente prueba 1
        # .even:nth-child(2) > td:nth-child(1) = Cliente prueba 2
        # .even:nth-child(3) > td:nth-child(1) = Cliente prueba 3
        # .even:nth-child(4) > td:nth-child(1) = Cliente prueba 4
        # 11 | Espera a que el expediente que se quiere modificar cargue y este disponible para presionar
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")))  # el expediente que abrimos
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")))
        # 12 | Presiona el expediente que se quiere crear el plan de pago
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(1) > td:nth-child(1)")
        self.driver.execute_script("arguments[0].click();", element1)

        # Creamos el plan de pago
        # 13 | Hace una espera para que le botón de crear plan este disponible
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".create-plan-button")))
        # 14 | Presiona el buton de crear plan
        element = self.driver.find_element(By.CSS_SELECTOR, ".create-plan-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 15 | Hace una espera para que le botón de confirmar este disponible para presionar
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
        # 16 | Presiona el botón de confirmar
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element)


        # El tercer paso del flujo es la aprobar el plan de pagos por cliente en el módulo de cliente
        # 1 | Abre el modulo de cliente
        self.driver.get("http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Hace una espera de 5 segundos para que cargue el módulo
        time.sleep(5)
        # 4 | Espera que este disponible el hipervinculo para ir al plan de pagos
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//li[2]/a/span")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a/span")))
        # 5 | Presiona el hipervinculo para ir al plan de pago
        element = self.driver.find_element(By.XPATH, "//li[2]/a/span")
        self.driver.execute_script("arguments[0].click();", element)
        # 6 | Presiona el botón para aproban plan de pagos
        element = self.driver.find_element(By.XPATH, "//div[5]/button")
        self.driver.execute_script("arguments[0].click();", element)
        # 7 | Presiona el botón de aceptar
        element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 8 | Hace una espera de 5 segundos para que se apruebe el plan de pagos
        time.sleep(5)
