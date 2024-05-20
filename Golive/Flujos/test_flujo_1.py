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


class TestFlujo1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_flujo_1(self):
        # Test name: flujo 1
        # Primera parte: Crea plan de pago
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
        # 12 | Espera que el botón de crear plan este disponible
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".create-plan-button")))
        # 13 | Presiona el botón de crear plan
        element = self.driver.find_element(By.CSS_SELECTOR, ".create-plan-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 14 | Espera que le botón de confirmar esté disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
        # 15 | Presiona el botón de confirmar la creación de plan
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element)

        # segunda parte: aprobar plan de pago cliente
        # Este paso posteriormente se eliminará porque el módulo cliente no estará para el GoLive
        # 1 | Abre el módulo de clientes
        self.driver.get("http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en pantalla completa
        self.driver.maximize_window()
        # 3 | Presiona el espacio de email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 4 | Digita el email
        self.driver.find_element(By.NAME, "emaiI").send_keys("prueba.cliente1.concasahome@yopmail.com")
        # 5 | Presiona el espacio de la contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 6 | Digita la contraseña
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | Presiona la tecla Enter
        self.driver.find_element(By.NAME, "passI").send_keys(Keys.ENTER)
        # 8 | Presiona el botón de iniciar sesión
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(10) > .initButtonLogin").click()
        time.sleep(10)
        # 9 | Espera que el botón del expediente esté cargado
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//li[2]/a/span")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a/span")))
        # 10 | Presiona el hipervinculo para ir al plan de pago
        element = self.driver.find_element(By.XPATH, "//li[2]/a/span")
        self.driver.execute_script("arguments[0].click();", element)
        # 11 | Presiona el botón para aproban plan de pagos
        element = self.driver.find_element(By.XPATH, "//div[5]/button")
        self.driver.execute_script("arguments[0].click();", element)
        # 12 | Presiona el botón de aceptar
        element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 13 | Hace una espera de 5 segundos para que se apruebe el plan de pagos
        time.sleep(5)


        # Segunda parte: Agrega pago de cuota
        # 1 | Abre el módulo de financiero
        self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Espera que el espacio del email este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, "emaiI")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "emaiI")))
        # 4 | Presiona el espacio de email en el espacio de email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 5 | Digita el email "asesor.financiero.concasa@yopmail.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("asesor.financiero.concasa@yopmail.com")
        # 6 | Digita la contraseña "123456"
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | Presiona el boton de iniciar sesión
        self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button").click()
        # 8 | Hace un mouse Over
        element = self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 9 | Hace un mouse Out
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 10 | Espera que el expediente este visible en la pantalla
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "9911")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "9911")))
        # 11 | Presiona el expediente al que le va a agregar la cuota
        # 9911: Cliente 1
        # 9921: Cliente 2
        # 9931: Cliente 3
        # 9941: Cliente 4
        element = self.driver.find_element(By.LINK_TEXT, "9911")
        self.driver.execute_script("arguments[0].click();", element)
        # 12 | Espera que  la sesión plan de pagos este visible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Plan de Pagos")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Plan de Pagos")))
        # 13 | Presiona la sesión plan de pagos dentro del expediente
        element = self.driver.find_element(By.LINK_TEXT, "Plan de Pagos")
        self.driver.execute_script("arguments[0].click();", element)
        # 14 | Presiona el botón agregar pago
        element = self.driver.find_element(By.CSS_SELECTOR, ".button-addClient")
        self.driver.execute_script("arguments[0].click();", element)
        # 15 | Espera que carguen los espacios para registrar el pago
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-input-modal-money")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-input-modal-money")))
        # 16 | Presiona el espacio "Monto abono"
        element = self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money")
        self.driver.execute_script("arguments[0].click();", element)
        # 17 | Digita la cantidad a abonar
        self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money").send_keys("750")
        # 18 | Espera que el espacio "Recibo Manual" este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")))
        # 19 | Presiona el espacio "Recibo Manual"
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")
        self.driver.execute_script("arguments[0].click();", element)
        # 20 | Digita "123" en el espacio "Recibo Manual"
        self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal").send_keys(
            "123")
        # 21 | Espera que el espacio "Referencia" este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")))
        # 22 | Presiona el espacio "Referencia"
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")
        self.driver.execute_script("arguments[0].click();", element)
        # 23 | Digita "123" en el espacio "Referencia"
        self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal").send_keys(
            "1234")
        # 24 | Espera que el espacio "Tipo de pago" este disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-check:nth-child(3) > .form-check-input")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-check:nth-child(3) > .form-check-input")))
        # 25 | Seleciona la opción "Efectivo" en el espacio "Tipo de pago"
        element = self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(3) > .form-check-input")
        self.driver.execute_script("arguments[0].click();", element)
        # 26 | Espera que el espacio "Notas" este disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-section-container > #comment")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container > #comment")))
        # 27 | Presiona el espacio "Notas"
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container > #comment")
        self.driver.execute_script("arguments[0].click();", element)
        # 28 | Digita "abc" en el espacio "Notas"
        self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container > #comment").send_keys("abc")
        # 29 | Espera que el botón "Registrar" esté disponible
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".large-modal-standard-button")))
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".large-modal-standard-button")))
        # 30 | Presiona el botón "Registrar"
        element = self.driver.find_element(By.CSS_SELECTOR, ".large-modal-standard-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 31 | Hace un mouseOver
        element = self.driver.find_element(By.CSS_SELECTOR, ".large-modal-standard-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 32 | Hace un mouseOut
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 33 | Espera que el botón de "Aceptar" este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".accept-button")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accept-button")))
        # 34 | Presiona el botón "Aceptar"
        element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 35 | Espera el botón de "ok" del modal que se realizó con exito el registro
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-button")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal-button")))
        # 36 | Presiona el botón "Ok"
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal-button")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
