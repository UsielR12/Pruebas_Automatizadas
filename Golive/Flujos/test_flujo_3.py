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


class TestFlujo3():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_flujo_3(self):
        # Test name: flujo 1
        # Primera parte: Crear plan de pago
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
            (By.CSS_SELECTOR, ".even:nth-child(3) > td:nth-child(1)")))  # el expediente que abrimos
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".even:nth-child(3) > td:nth-child(1)")))
        # 11 | Presiona el expediente al que se va a crear el plan de pago
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(3) > td:nth-child(1)")
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
        self.driver.find_element(By.NAME, "emaiI").send_keys("prueba.cliente3.concasahome@yopmail.com")
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


        # Segunda parte: crear desistimiento
        # 1 | Abre el módulo de financiero
        self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Espera que el espacio del email este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, "emaiI")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "emaiI")))
        # 4 | Presiona el espacio de email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 5 | Digita el email "asesor.financiero.concasa@yopmail.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("asesor.financiero.concasa@yopmail.com")
        # 6 | Presiona el espacio de contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 7 | Digita la contraseña "123456"
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 8 | Presiona el boton de iniciar sesión
        self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button").click()
        # 9 | Espera que la sección de expedientes este cargada
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".card-body:nth-child(1)")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-body:nth-child(1)")))
        # 10 | Presiona la sección de expedientes
        element = self.driver.find_element(By.CSS_SELECTOR, ".card-body:nth-child(1)")
        self.driver.execute_script("arguments[0].click();", element)
        # 11 | Espera que el expediente que se va a seleccionar este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "9931")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "9931")))
        # 12 | Presiona el expediente que se va a desistir
        # 9911: Cliente 1
        # 9921: Cliente 2
        # 9931: Cliente 3
        # 9941: Cliente 4
        element = self.driver.find_element(By.LINK_TEXT, "9931")
        self.driver.execute_script("arguments[0].click();", element)
        # 13 | Espera que la sección de "Información" del expediente cargue
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Información")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Información")))
        # 14 | Hace un move to element
        element2 = self.driver.find_element(By.LINK_TEXT, "Información")
        actions = ActionChains(self.driver)
        actions.move_to_element(element2).perform()
        # 15 | Hace un moveOut
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 16 | Presiona el botón "desistir"
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".button-desist")
        self.driver.execute_script("arguments[0].click();", element1)
        # 17 | Presiona el combobox de "seleccionar razón"
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container #dModal-Toggle")
        self.driver.execute_script("arguments[0].click();", element)
        # 18 | Presiona la razón del desistimiento
        element = self.driver.find_element(By.LINK_TEXT, "Capacidad de pago insuficiente")
        self.driver.execute_script("arguments[0].click();", element)
        # 18 | Digita la fecha del desistimiento
        self.driver.find_element(By.CSS_SELECTOR, ".picker-input_modal input").send_keys("5/6/2024")
        # 19 | Presiona el espacio "Monto de devolución"
        element = self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money")
        self.driver.execute_script("arguments[0].click();", element)
        # 20 | Digita el monto de devolución
        self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money").send_keys("00")
        # 21 | Presiona el espacio "Notas"
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container .observationText")
        self.driver.execute_script("arguments[0].click();", element)
        # 22 | Digita la nota del desistimiento
        self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container .observationText").send_keys(
            "No hay pago suficiente")
        # 23 | Presiona el espacio de registrar desistimiento
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
        self.driver.execute_script("arguments[0].click();", element)
        # 24 | Presiona el botón "Registrar"
        element = self.driver.find_element(By.CSS_SELECTOR, ".large-modal-standard-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 25 | Presiona el botón de aceptar y se crea el desistimiento
        element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 26 | Espera que el modal de que se realizó con exito aparezca
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
        # 27 | Presiona "ok" del último modal que se realizo con exito
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element)
        # 28 | Presiona el botón de perfil
        element = self.driver.find_element(By.CSS_SELECTOR, ".c-pointer")
        self.driver.execute_script("arguments[0].click();", element)
        # 29 | Presiona el botón de cerrar sesión
        element = self.driver.find_element(By.CSS_SELECTOR, ".ai-icon:nth-child(3)")
        self.driver.execute_script("arguments[0].click();", element)
        # 30 | hace una espera de 8 segundos
        time.sleep(8)

        # Tercera parte: rechazar el desistimiento
        # 1 | Abre el módulo de financiero
        self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com/login")
        # 2 | Pone el navegador en tamaño completo
        self.driver.maximize_window()
        # 3 | Espera que el espacio del email este disponible
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, "emaiI")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "emaiI")))
        # 4 | Presiona el espacio de email en el espacio de email
        self.driver.find_element(By.NAME, "emaiI").click()
        # 5 | Digita el email "usiel.ramirez@concasa.com"
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        # 6 | Presiona el espacio de contraseña
        self.driver.find_element(By.NAME, "passI").click()
        # 7 | Digita la contraseña "123456"
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 8 | Presiona el boton de iniciar sesión
        self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button").click()
        # 9 | Hace un mouse Over
        element = self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 10 | Hace un mouse Out
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 11 | Espera que cargue el botón de "Aprobaciones"
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Aprobaciones")))
        # 12 | Presiona la sección de "Aprobaciones" del menu hamburguesa
        element = self.driver.find_element(By.LINK_TEXT, "Aprobaciones")
        self.driver.execute_script("arguments[0].click();", element)
        # 13 | Presiona la sección de Desistimientos
        element = self.driver.find_element(By.LINK_TEXT, "Desistimientos")
        self.driver.execute_script("arguments[0].click();", element)
        # 14 | Espera que cargue
        time.sleep(5)
        # 15 | Va la segunda página de los desistimientos
        element = self.driver.find_element(By.CSS_SELECTOR, ".fade:nth-child(3) .pagination-button-pwa:nth-child(4)")
        self.driver.execute_script("arguments[0].click();", element)
        # 16 | Espera que el expediente que se quiere presionar este disponible
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "37")))
        # 17 | Presiona el expediente que se a gestionar el desistimiento
        element = self.driver.find_element(By.LINK_TEXT, "37")
        self.driver.execute_script("arguments[0].click();", element)
        # 18 | Espera que el botón de "Aprobar" este disponible
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".reject-button")))
        # 19 | Presiona el botón de "Aprobar"
        element = self.driver.find_element(By.CSS_SELECTOR, ".reject-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 20 | Espera que el botón de "Sí" este disponible del modal de aceptar desistimiento
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".actionsContainer > .accept-button")))
        # 21 | Presiona el botón de "Sí" del modal de aceptar desistimiento
        element = self.driver.find_element(By.CSS_SELECTOR, ".actionsContainer > .accept-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 22 | Espera que el botón de "Ok" este disponible del modal de se realizó con exito el desistimiento
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        # 23 | Presiona el botón de "Ok" del modal de se realizó con exito el desistimiento
        element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element)
