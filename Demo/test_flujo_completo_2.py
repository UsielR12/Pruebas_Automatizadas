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


class Testflujocompleto2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_flujo_completo_2(self):
        # Test name: crear el perfil del cliente
        # Step # | name | target | value
        # 1 | open | http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login |
        self.driver.get("http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login")
        # 2 | setWindowSize | 1920x1080 |
        self.driver.maximize_window()
        # 3 | click | name=emaiI |
        self.driver.find_element(By.NAME, "emaiI").click()
        # 4 | type | name=emaiI | prueba.cliente1.concasahome@yopmail.com
        self.driver.find_element(By.NAME, "emaiI").send_keys("prueba.cliente2.concasahome@yopmail.com")
        # 5 | click | name=passI |
        self.driver.find_element(By.NAME, "passI").click()
        # 6 | type | name=passI | 123456
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | click | css=div:nth-child(10) > .initButtonLogin |
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(10) > .initButtonLogin").click()
        # 8 | pause | 8000 |
        time.sleep(15)
        self.driver.find_element(By.XPATH, "//button").click()
        self.driver.find_element(By.XPATH, "//button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        self.driver.find_element(By.XPATH, "//section/div/div/div[2]/div/div").click()
        # 10 | click | id=idNumber |
        self.driver.find_element(By.ID, "idNumber").clear()
        self.driver.find_element(By.ID, "idNumber").click()
        # 11 | type | id=idNumber | 117970499
        self.driver.find_element(By.ID, "idNumber").send_keys("117970499")
        # 12 | click | xpath=//button |
        self.driver.find_element(By.XPATH, "//button").click()
        # 13 | waitForElementEditable | xpath=//button | 30000
        # time.sleep(10)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button")))
        # 14 | click | xpath=//button |
        self.driver.find_element(By.XPATH, "//button").click()

        self.driver.find_element(By.XPATH, "//section/div/div/div/div/div").click()
        # element1 = self.driver.find_element(By.CSS_SELECTOR, ".css-1gtu0rj-indicatorContainer")
        # self.driver.execute_script("arguments[0].click();", element1)

        # 17 | type | id=react-select-4-input | 506
        # self.driver.find_element(By.XPATH, "//section/div/div/div/div/div[2]/div").clear()
        self.driver.find_element(By.XPATH, "//div[52]/div").click()
        # 18 | sendKeys | id=react-select-4-input | ${KEY_ENTER}
        # self.driver.find_element(By.XPATH, "//section/div/div/div/div/div[2]/div").send_keys(Keys.ENTER)
        # 19 | click | css=.inputContainer:nth-child(1) .ml-3 |
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").click()
        # 20 | type | css=.inputContainer:nth-child(1) .ml-3 | 1234 5678
        self.driver.find_element(By.CSS_SELECTOR, ".inputContainer:nth-child(1) .ml-3").send_keys("1234 5678")
        # 21 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 22 | click | css=.btnStyle-0-2-10:nth-child(1) |
        self.driver.find_element(By.XPATH, "//button").click()
        # 23 | click | xpath=//div[2]/div/div[2]/div/div/div/div/div/div/div/div |
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div/div/div/div/div").click()
        # 24 | sendKeys | id=react-select-6-input | ${KEY_ENTER}
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div/div").click()
        # 25 | click | xpath=//div[2]/div/div[2]/div/div[2]/div/div/div/div/div |
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/div/div/div").click()
        # 26 | sendKeys | id=react-select-7-input | ${KEY_ENTER}
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div[2]/div/div").click()
        # 27 | click | xpath=//div[3]/div/div/div/div/div |
        self.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div").click()
        # 28 | sendKeys | id=react-select-8-input | ${KEY_ENTER}
        self.driver.find_element(By.XPATH, "//div/div[3]/div/div/div/div[2]/div/div").click()
        # 29 | click | id=exactDirection |
        self.driver.find_element(By.ID, "exactDirection").clear()
        self.driver.find_element(By.ID, "exactDirection").click()
        # 30 | type | id=exactDirection | abcdfg
        self.driver.find_element(By.ID, "exactDirection").send_keys("abcdfg")
        # 31 | sendKeys | id=exactDirection | ${KEY_ENTER}
        self.driver.find_element(By.ID, "exactDirection").send_keys(Keys.ENTER)
        # 32 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 33 | click | css=.btnStyle-0-2-4:nth-child(1) |
        self.driver.find_element(By.XPATH, "//button").click()
        # 34 | click | id=companyName |
        self.driver.find_element(By.ID, "companyName").clear()
        self.driver.find_element(By.ID, "companyName").click()
        # 35 | type | id=companyName | intel
        self.driver.find_element(By.ID, "companyName").send_keys("intel")
        # 36 | click | css=.businessInfo-phoneInput |
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").click()
        # 37 | type | css=.businessInfo-phoneInput | 8765 4321
        self.driver.find_element(By.CSS_SELECTOR, ".businessInfo-phoneInput").send_keys("8765 4321")
        # 38 | click | id=addressCompany |
        self.driver.find_element(By.ID, "addressCompany").clear()
        self.driver.find_element(By.ID, "addressCompany").click()
        # 39 | type | id=addressCompany | abcdfg
        self.driver.find_element(By.ID, "addressCompany").send_keys("abcdfg")
        # 40 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 41 | click | id=companyName |
        self.driver.find_element(By.ID, "companyName").clear()
        self.driver.find_element(By.ID, "companyName").click()
        # 42 | type | id=companyName | ingeniero
        self.driver.find_element(By.ID, "companyName").send_keys("ingeniero")
        # 43 | click | css=.css-1t5ue5z |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        # 44 | click | id=react-select-12-option-0 |
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div/div").click()
        # 45 | click | id=timeCompany |
        self.driver.find_element(By.ID, "timeCompany").clear()
        self.driver.find_element(By.ID, "timeCompany").click()
        # 46 | type | id=timeCompany | 5
        self.driver.find_element(By.ID, "timeCompany").send_keys("5")
        # 47 | sendKeys | id=timeCompany | ${KEY_ENTER}
        self.driver.find_element(By.ID, "timeCompany").send_keys(Keys.ENTER)
        # 48 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 49 | click | css=.css-g1nrkn |
        self.driver.find_element(By.CSS_SELECTOR, ".css-g1nrkn").click()
        # 50 | click | id=react-select-13-option-0 |
        self.driver.find_element(By.XPATH, "//section/div/div/div/div[2]/div/div").click()
        # 51 | click | css=.formInput:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").click()
        # 52 | type | css=.formInput:nth-child(2) | 5,000
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").send_keys("5,000")
        # 53 | sendKeys | css=.formInput:nth-child(2) | ${KEY_ENTER}
        self.driver.find_element(By.CSS_SELECTOR, ".formInput:nth-child(2)").send_keys(Keys.ENTER)
        # 54 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 55 | click | css=.btnStyle-0-2-4:nth-child(2) |
        element = self.driver.find_element(By.XPATH, "//button[2]")
        self.driver.execute_script("arguments[0].click();", element)
        # 56 | click | css=.btnStyle-0-2-4:nth-child(1) |
        self.driver.find_element(By.XPATH, "//button").click()
        # 57 | click | css=.css-1t5ue5z |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1t5ue5z").click()
        # 58 | click | id=react-select-14-option-0 |
        self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div/div").click()
        # 59 | click | css=.ml-3 |
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").click()
        # 60 | type | css=.ml-3 | 5,000
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").send_keys("5,000")
        # 61 | sendKeys | css=.ml-3 | ${KEY_ENTER}
        self.driver.find_element(By.CSS_SELECTOR, ".ml-3").send_keys(Keys.ENTER)
        # 62 | click | css=.btnNext |
        self.driver.find_element(By.CSS_SELECTOR, ".btnNext").click()
        # 63 | click | css=i |
        self.driver.find_element(By.CSS_SELECTOR, "i").click()

        # Termina el proceso de completar usuario
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex:nth-child(5) > .font-lato").click()
        time.sleep(5)


        #empieza la creación del plan de pagos del cliente
        # Inicio de sesión
        self.driver.get("http://concasa-real-estate.s3-website-us-east-1.amazonaws.com/")
        self.driver.maximize_window()
        time.sleep(5)
        element = self.driver.find_element(By.NAME, "emaiI")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        element = self.driver.find_element(By.NAME, "passI")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        element = self.driver.find_element(By.CSS_SELECTOR, ".section-container:nth-child(6) > .mr-2")
        self.driver.execute_script("arguments[0].click();", element)

        # Redirección al apartado de gestión de ventas
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "Gestión de ventas")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Gestión de ventas")))
        element = self.driver.find_element(By.LINK_TEXT, "Gestión de ventas")
        self.driver.execute_script("arguments[0].click();", element)

        # Selección del expediente que vamos a crearle un plan de pagos
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(2)")))  # el expediente que abrimos
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(2)")))
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(2)")
        self.driver.execute_script("arguments[0].click();", element1)

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".number-input-container")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".number-input-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").clear()
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".number-input-container")
        self.driver.execute_script("arguments[0].click();", element1)
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.BACKSPACE)

        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys("15")
        self.driver.find_element(By.CSS_SELECTOR, ".number-input-container").send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-area-input-container")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-area-input-container")))
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".text-area-input-container")
        self.driver.execute_script("arguments[0].click();", element1)
        self.driver.find_element(By.CSS_SELECTOR, ".text-area-input-container").send_keys("necesidad de más cuotas")

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".send-to-aprove-button")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".send-to-aprove-button")))
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".send-to-aprove-button")
        self.driver.execute_script("arguments[0].click();", element1)

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm")))
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
        self.driver.execute_script("arguments[0].click();", element1)

        # Test name: test_aprobar_plan_de_pago_SAF
        # Step # | name | target | value
        # 1 | open | http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com |
        self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.maximize_window()  # Pone el navegador en tamaño completo
        # 3 | click | name=emaiI |
        time.sleep(5)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, "emaiI")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "emaiI")))
        element = self.driver.find_element(By.NAME, "emaiI")
        self.driver.execute_script("arguments[0].click();", element)
        # 4 | type | name=emaiI | usiel.ramirez@concasa.com
        self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
        # 5 | click | name=passI |
        element = self.driver.find_element(By.NAME, "passI")
        self.driver.execute_script("arguments[0].click();", element)
        # 6 | type | name=passI | 123456
        self.driver.find_element(By.NAME, "passI").send_keys("123456")
        # 7 | click | css=.textPassword > .beginning-button |
        element = self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button")
        self.driver.execute_script("arguments[0].click();", element)
        # 8 | waitForElementPresent | linkText=Aprobaciones | 30000
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//li[4]/a")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[4]/a")))
        # 9 | click | linkText=Aprobaciones |
        element = self.driver.find_element(By.XPATH, "//li[4]/a")
        self.driver.execute_script("arguments[0].click();", element)

        # 10 | click | linkText=9091 | Aquí se selecciona el expediente que se va a aprobar
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.LINK_TEXT, "9921")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "9921")))
        element = self.driver.find_element(By.LINK_TEXT, "9921")
        self.driver.execute_script("arguments[0].click();", element)

        # 11 | click | id=comment |
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "comment")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "comment")))
        element = self.driver.find_element(By.ID, "comment")
        self.driver.execute_script("arguments[0].click();", element)

        # 12 | type | id=comment | es aceptable
        self.driver.find_element(By.ID, "comment").send_keys("es aceptable")

        element = self.driver.find_element(By.XPATH, "//button[2]")
        self.driver.execute_script("arguments[0].click();", element)

        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/button[2]")))
        element = self.driver.find_element(By.XPATH, "//div[3]/button[2]")
        self.driver.execute_script("arguments[0].click();", element)


        # Test name: test_aprobar_plan_de_pago_cliente
        # Step # | name | target | value
        # 1 | open | http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login |
        self.driver.get("http://concasa-preventa.s3-website-us-east-1.amazonaws.com/login")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.maximize_window()
        time.sleep(5)
        # 9 | click | css=li:nth-child(2) .nav-text |
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//li[2]/a/span")))
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a/span")))
        element = self.driver.find_element(By.XPATH, "//li[2]/a/span")
        self.driver.execute_script("arguments[0].click();", element)


        # Aprueba el plan de pagos
        element = self.driver.find_element(By.XPATH, "//div[5]/button")
        self.driver.execute_script("arguments[0].click();", element)


        element = self.driver.find_element(By.CSS_SELECTOR, ".accept-button")
        self.driver.execute_script("arguments[0].click();", element)

        time.sleep(5)
