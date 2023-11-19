from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



# Create your tests here.
class testCancelation(LiveServerTestCase):
  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000')

  def testCancelationCourse(self):

    user = self.driver.find_element(by=By.ID,value='id_username')
    password = self.driver.find_element(by=By.ID,value='id_password')
   
    submit = self.driver.find_element(by=By.ID, value='inicio')

    #populate the form with data
    user.send_keys('daniel')
    password.send_keys('1234')

    #submit form
    submit.send_keys(Keys.RETURN)


    submit = self.driver.find_element(by=By.ID, value='cancelacion')
    submit.send_keys(Keys.RETURN)

    #search student
    time.sleep(2)
    submit = self.driver.find_element(by=By.XPATH, value="//input[@type='search']")
    submit.send_keys('A00381293')

    time.sleep(2)
    submit = self.driver.find_element(by=By.ID, value='selection')
  
    #submit form
    submit.send_keys(Keys.RETURN)

    time.sleep(2)
    
    submit2 = self.driver.find_element(by=By.ID, value='cancelation')
  
    submit2.send_keys(Keys.RETURN)
    time.sleep(2)
    
    elemento_h3 = self.driver.find_element(By.TAG_NAME, "h3")

    # Obtén el contenido actual del elemento
    contenido_actual = elemento_h3.text
       
    contenido_esperado = "MENU CANCELACIONES"
    self.assertEqual(contenido_actual, contenido_esperado)

    self.driver.quit()
    