# Generated by Selenium IDE
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



class TestTestcreardesistimientofinanciero():
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


  def test_testcreardesistimientofinanciero(self):
    # Test name: test_crear_desistimiento_financiero
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
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".card-body:nth-child(1)")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-body:nth-child(1)")))
    # 10 | Presiona la sección de expedientes
    element = self.driver.find_element(By.CSS_SELECTOR, ".card-body:nth-child(1)")
    self.driver.execute_script("arguments[0].click();", element)
    # 11 | Espera que el expediente que se va a seleccionar este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "9911")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "9911")))
    # 12 | Presiona el expediente que se va a desistir
    element = self.driver.find_element(By.LINK_TEXT, "9911")
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
    self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container .observationText").send_keys("No hay pago suficiente")
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
    # 28 | Hace una espera de 4 segundos
    time.sleep(4)

