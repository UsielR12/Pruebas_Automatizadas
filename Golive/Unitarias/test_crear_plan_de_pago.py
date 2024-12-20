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

class TestCrearPlanDePago():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window() #Pone el navegador en tamaño completo
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_crear_plan_de_pago(self):
    # Test name: test_crear_desistimiento_financiero
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
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(1)"))) # el expediente que abrimos
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(1)")))
    # 11 | Presiona el expediente al que se va a crear el plan de pago
    element1 = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(1)")
    self.driver.execute_script("arguments[0].click();", element1)
    # 12 | Espera que el botón de crear plan este disponible
    WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".create-plan-button")))
    # 13 | Presiona el botón de crear plan
    element = self.driver.find_element(By.CSS_SELECTOR, ".create-plan-button")
    self.driver.execute_script("arguments[0].click();", element)
    # 14 | Espera que le botón de confirmar esté disponible
    WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
    # 15 | Presiona el botón de confirmar la creación de plan
    element = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
    self.driver.execute_script("arguments[0].click();", element)



