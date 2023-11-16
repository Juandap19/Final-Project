from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from follow_students.models import *

class testAlimentacion(LiveServerTestCase):
  
  def setUp(self):

      self.driver = webdriver.Chrome()
      self.driver.get('http://127.0.0.1:8000/apoyo_financiero_alimentacion/')


  def test_sucess_expend(self):

    student_code = self.driver.find_element(by=By.ID, value = 'id_student_code')
    money_quantity = self.driver.find_element(by = By.ID, value =  'id_money_quantity')
    acumulate_time = self.driver.find_element(by = By.ID, value =  'id_acumulate_time')
    select_time = self.driver.find_element(by = By.ID, value =  'id_select_time')
     
    student_code.send_keys('A00381293')
    money_quantity.send_keys('10')
    acumulate_time.send_keys('13')
    select_time.send_keys('1')

    alimentacion_btn = self.driver.find_element(by = By.ID, value = 'alimentacion_btn')

    alimentacion_btn.send_keys(Keys.RETURN)


    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "swal2-title"))
    )

    contenido_actual = self.driver.find_element(by=By.ID, value='swal2-title')
    texto_contenido_actual = contenido_actual.text
    contenido_esperado = "Proceso Completado"
    self.assertEqual(texto_contenido_actual, contenido_esperado)

  def test_post_student_not_found(self):

    student_code = self.driver.find_element(by=By.ID, value = 'id_student_code')
    money_quantity = self.driver.find_element(by = By.ID, value =  'id_money_quantity')
    acumulate_time = self.driver.find_element(by = By.ID, value =  'id_acumulate_time')
    select_time = self.driver.find_element(by = By.ID, value =  'id_select_time')
        
    student_code.send_keys('A00381294')
    money_quantity.send_keys('100000000')
    acumulate_time.send_keys('13')
    select_time.send_keys('1')

    alimentacion_btn = self.driver.find_element(by = By.ID, value = 'alimentacion_btn')
    alimentacion_btn.send_keys(Keys.RETURN)
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "swal2-title"))
    )


    contenido_actual = self.driver.find_element(by=By.ID, value='swal2-title')
    texto_contenido_actual = contenido_actual.text
    contenido_esperado = "El codigo del estudiante A00381294 no existe"
    self.assertEqual(texto_contenido_actual, contenido_esperado)

  def test_post_insufficient_funds(self):

    student_code = self.driver.find_element(by=By.ID, value = 'id_student_code')
    money_quantity = self.driver.find_element(by = By.ID, value =  'id_money_quantity')
    acumulate_time = self.driver.find_element(by = By.ID, value =  'id_acumulate_time')
    select_time = self.driver.find_element(by = By.ID, value =  'id_select_time')
        
    student_code.send_keys('A00381293')
    money_quantity.send_keys('1200000000')
    acumulate_time.send_keys('13')
    select_time.send_keys('1')

    alimentacion_btn = self.driver.find_element(by = By.ID, value = 'alimentacion_btn')

    alimentacion_btn.send_keys(Keys.RETURN)
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "swal2-title"))
    )


    contenido_actual = self.driver.find_element(by=By.ID, value='swal2-title')
    texto_contenido_actual = contenido_actual.text
    contenido_esperado = "Fondos insuficientes de alimentación para registrar el pago"
    self.assertEqual(texto_contenido_actual, contenido_esperado)
