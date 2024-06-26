# Generated by Selenium IDE
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

class TestTestagregarpagodecuotafinanciero():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()  # Pone el navegador en tamaño completo
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testagregarpagodecuotafinanciero(self):
    # Test name: test_agregar_pago_de_cuota_financiero
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
    element = self.driver.find_element(By.LINK_TEXT, "9911")
    self.driver.execute_script("arguments[0].click();", element)
    # 12 | Espera que  la sesión plan de pagos este visible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Plan de Pagos")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Plan de Pagos")))
    # 13 | Presiona la sesión plan de pagos dentro del expediente
    element = self.driver.find_element(By.LINK_TEXT, "Plan de Pagos")
    self.driver.execute_script("arguments[0].click();", element)
    # 14 | Presiona el botón agregar pago
    element = self.driver.find_element(By.CSS_SELECTOR , ".button-addClient")
    self.driver.execute_script("arguments[0].click();", element)
    # 15 | Espera que carguen los espacios para registrar el pago
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-input-modal-money")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-input-modal-money")))
    # 16 | Presiona el espacio "Monto abono"
    element = self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money")
    self.driver.execute_script("arguments[0].click();", element)
    # 17 | Digita la cantidad a abonar
    self.driver.find_element(By.CSS_SELECTOR, ".text-input-modal-money").send_keys("750")
    # 18 | Espera que el espacio "Recibo Manual" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")))
    # 19 | Presiona el espacio "Recibo Manual"
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal")
    self.driver.execute_script("arguments[0].click();", element)
    # 20 | Digita "123" en el espacio "Recibo Manual"
    self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(2) .text-input-modal").send_keys("123")
    # 21 | Espera que el espacio "Referencia" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")))
    # 22 | Presiona el espacio "Referencia"
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal")
    self.driver.execute_script("arguments[0].click();", element)
    # 23 | Digita "123" en el espacio "Referencia"
    self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container:nth-child(3) .text-input-modal").send_keys("1234")
    # 24 | Espera que el espacio "Tipo de pago" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-check:nth-child(1) > .form-check-input")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-check:nth-child(1) > .form-check-input")))
    # 25 | Seleciona la opción "Transferencia Bancaria" en el espacio "Tipo de pago"
    element = self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(1) > .form-check-input")
    self.driver.execute_script("arguments[0].click();", element)
    # 26 | Espera que el espacio "Seleccionar Banco" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(1) > .dropdown > #dModal-Toggle")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > .dropdown > #dModal-Toggle")))
    # 27 | Selecciona el espacio "Seleccionar Banco"
    element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .dropdown > #dModal-Toggle")
    self.driver.execute_script("arguments[0].click();", element)
    # 28 | Espera que el espacio de la lista de seleccionar banco este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "BCT-CRC")))
    # 29 | Selecciona la opción del listbox de Seleccionar Banco
    element = self.driver.find_element(By.LINK_TEXT, "BCT-CRC")
    self.driver.execute_script("arguments[0].click();", element)
    # 30 | Espera que el espacio "Notas" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-section-container > #comment")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-section-container > #comment")))
    # 31 | Presiona el espacio "Notas"
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container > #comment")
    self.driver.execute_script("arguments[0].click();", element)
    # 32 | Digita "abc" en el espacio "Notas"
    self.driver.find_element(By.CSS_SELECTOR, ".modal-section-container > #comment").send_keys("abc")
    # 33 | Espera que el botón "Registrar" esté disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".large-modal-standard-button")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".large-modal-standard-button")))
    # 34 | Presiona el botón "Registrar"
    element = self.driver.find_element(By.CSS_SELECTOR, ".large-modal-standard-button")
    self.driver.execute_script("arguments[0].click();", element)
    # 35 | Hace un mouseOver
    element = self.driver.find_element(By.CSS_SELECTOR, ".large-modal-standard-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 36 | Hace un mouseOut
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 37 | Espera que el botón de "Aceptar" este disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".accept-button")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accept-button")))
    # 38 | Presiona el botón "Aceptar"
    element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
    self.driver.execute_script("arguments[0].click();", element)
    # 39 | Espera el botón de "ok" del modal que se realizó con exito el registro
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-button")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal-button")))
    # 40 | Presiona el botón "Ok"
    element = self.driver.find_element(By.CSS_SELECTOR, ".swal-button")
    self.driver.execute_script("arguments[0].click();", element)
    time.sleep(3)


  
