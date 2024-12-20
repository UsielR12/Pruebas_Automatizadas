# Generated by Selenium IDE
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

class TestTesteliminarasesorfinancieroFinanciero():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testeliminarasesorfinancieroFinanciero(self):
    # Test name: test_eliminar_asesor_financiero_Financiero
    # Step # | name | target | value
    # 1 | open | http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com/login | 
    self.driver.get("http://concasa-financial-advisor.s3-website-us-east-1.amazonaws.com/login")
    # 2 | setWindowSize | 1920x1080 | 
    self.driver.maximize_window()
    # 3 | click | name=emaiI | 
    self.driver.find_element(By.NAME, "emaiI").click()
    # 4 | type | name=emaiI | usiel.ramirez@concasa.com
    self.driver.find_element(By.NAME, "emaiI").send_keys("usiel.ramirez@concasa.com")
    # 5 | click | name=passI | 
    self.driver.find_element(By.NAME, "passI").click()
    # 6 | type | name=passI | 123456
    self.driver.find_element(By.NAME, "passI").send_keys("123456")
    # 7 | click | css=.textPassword > .beginning-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button").click()
    # 8 | mouseOver | css=.textPassword > .beginning-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".textPassword > .beginning-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | css=.textPassword > .beginning-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 10 | waitForElementPresent | linkText=Usuarios | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Usuarios")))
    # 11 | click | linkText=Usuarios | 
    self.driver.find_element(By.LINK_TEXT, "Usuarios").click()
    # 12 | waitForElementEditable | id=dropdown-basic | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "dropdown-basic")))
    # 13 | pause | 2000 | 
    time.sleep(2)
    # 14 | click | id=dropdown-basic | 
    self.driver.find_element(By.ID, "dropdown-basic").click()
    # 15 | pause | 1000 | 
    time.sleep(1)
    # 16 | click | id=4 | 
    self.driver.find_element(By.ID, "4").click()
    # 17 | pause | 2000 | 
    time.sleep(2)
    # 18 | click | css=tr:nth-child(6) .userOptions-container svg:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) .userOptions-container svg:nth-child(2)").click()
  
