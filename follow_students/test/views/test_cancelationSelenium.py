from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Create your tests here.
class testCancelation(LiveServerTestCase):
  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000')

  def testCancelationCourse(self):

    user = self.driver.find_element(by=By.ID,value='id_username')
    password = self.driver.find_element(by=By.ID,value='id_password')
   
    submit = self.driver.find_element(by=By.ID, value='inicio')

    #populate the form with data
    user.send_keys('2')
    password.send_keys('2')

    #submit form
    submit.send_keys(Keys.RETURN)


    submit = self.driver.find_element(by=By.ID, value='cancelacion')
    submit.send_keys(Keys.RETURN)

    submit = self.driver.find_element(by=By.ID, value='selection')
  
    #submit form
    submit.send_keys(Keys.RETURN)
    
    submit2 = self.driver.find_element(by=By.ID, value='cancelation')
  
    submit2.send_keys(Keys.RETURN)
    
    elemento_h3 = self.driver.find_element(By.TAG_NAME, "h3")

    # Obtén el contenido actual del elemento
    contenido_actual = elemento_h3.text
       
    contenido_esperado = "MENU CANCELACIONES"
    self.assertEqual(contenido_actual, contenido_esperado)
    