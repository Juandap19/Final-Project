from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

class testSeleniumLogin(LiveServerTestCase):

    def testValidLogin(self):

        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000')
        time.sleep(2)

        input_username = driver.find_element(By.ID, 'id_username')
        input_password = driver.find_element(By.ID, 'id_password')

        input_username.send_keys('diego')
        input_password.send_keys('1234')

        button_xpath = '/html/body/main/div/section[1]/article/form/button'
        submit_button = driver.find_element(By.XPATH, button_xpath)
        submit_button.click()

        time.sleep(2)

        elemento_h3 = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/h3")
        contenido_actual = elemento_h3.text
        contenido_esperado = "PANEL DE CONTROL"
        self.assertEqual(contenido_actual, contenido_esperado)

        driver.quit()
    
    def testInvalidLogin(self):

        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000')
        time.sleep(2)

        input_username = driver.find_element(By.ID, 'id_username')
        input_password = driver.find_element(By.ID, 'id_password')

        input_username.send_keys('diego')
        input_password.send_keys('1312312312')

        button_xpath = '/html/body/main/div/section[1]/article/form/button'
        submit_button = driver.find_element(By.XPATH, button_xpath)
        submit_button.click()

        time.sleep(2)

        elemento_h6 = driver.find_element(By.XPATH, "/html/body/main/div/section[1]/article/div/h6")
        contenido_actual = elemento_h6.text
        contenido_esperado = "Usuario o Contraseña incorrectos"
        self.assertEqual(contenido_actual, contenido_esperado)

        driver.quit()