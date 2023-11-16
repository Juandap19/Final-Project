from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


class RequestUpdSeleniumTest(LiveServerTestCase):
    
    #Sin archivo
    def test_RequestUpdatePage(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/requestupd/')
        time.sleep(2)
        
        receiver = driver.find_element(By.ID, 'id_destinatario')
        matter = driver.find_element(By.ID, 'id_asunto')
        message = driver.find_element(By.ID, 'id_mensaje')
        summit_button = driver.find_element(By.ID, 'send-button')
        receiver.send_keys('darwinlenis@gmail.com')
        matter.send_keys('Pruebas Unitarias :(((')
        message.send_keys('Esto es un mensaje de prueba')
        
        summit_button.click()
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Se ha enviado correctamente')

        driver.quit()
    
    #Con archivo
    def test_RequestUpdatePageFile(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/requestupd/')
        time.sleep(2)
        
        receiver = driver.find_element(By.ID, 'id_destinatario')
        matter = driver.find_element(By.ID, 'id_asunto')
        message = driver.find_element(By.ID, 'id_mensaje')
        file = driver.find_element(By.ID, 'id_archivo')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        receiver.send_keys('darwinlenis@gmail.com')
        matter.send_keys('Pruebas Unitarias :(((')
        message.send_keys('Esto es un mensaje de prueba')
        file.send_keys('C:\\Users\\Darwin Lenis\\OneDrive\\Escritorio\\Universidad\\5to Semestre\\Proyecto Integrador\\GitHub\\Final-Project\\follow_students\\static\\images\\campus_ICESI.jpg')
        
        summit_button.click()
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Se ha enviado correctamente')

        driver.quit()
        
        
    """
    def test_RequestUpdatePageInvalid(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/requestupd/')
        time.sleep(2)
        
        receiver = driver.find_element(By.ID, 'id_destinatario')
        matter = driver.find_element(By.ID, 'id_asunto')
        message = driver.find_element(By.ID, 'id_mensaje')
        file = driver.find_element(By.ID, 'id_archivo')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        receiver.send_keys('correo-erroneo')
        matter.send_keys('Pruebas Unitarias :(((')
        message.send_keys('Esto es un mensaje de prueba')
        file.send_keys('C:\\Users\\Darwin Lenis\\OneDrive\\Escritorio\\Universidad\\5to Semestre\\Proyecto Integrador\\GitHub\\Final-Project\\follow_students\\static\\images\\campus_ICESI.jpg')
        
        summit_button.click()
        
        error_message = driver.find_element(By.CLASS_NAME, 'error-message')
        self.assertTrue(error_message.is_displayed())
        
        driver.quit()
    """
        
        
        
    