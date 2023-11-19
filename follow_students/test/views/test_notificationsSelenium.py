from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Create your tests here.
class testSinginForm(LiveServerTestCase):
  def setUp(self):

      self.driver = webdriver.Chrome()


      self.driver.get('http://127.0.0.1:8000')

  def testNotification(self):

    user = self.driver.find_element(by=By.ID,value='id_username')
    password = self.driver.find_element(by=By.ID,value='id_password')
   
    submit = self.driver.find_element(by=By.ID, value='inicio')

    #populate the form with data
    user.send_keys('diego')
    password.send_keys('1234')

    #submit form
    submit.send_keys(Keys.RETURN)


    submit = self.driver.find_element(by=By.ID, value='Notificacion')
    submit.send_keys(Keys.RETURN)
    
    elemento_h3 = self.driver.find_element(By.TAG_NAME, "h3")

    # Obtén el contenido actual del elemento
    contenido_actual = elemento_h3.text
       
    contenido_esperado = "NOTIFICACIONES"
    self.assertEqual(contenido_actual, contenido_esperado)

    #check result; page source looks at entire html document
