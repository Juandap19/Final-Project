from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from follow_students.models import *
import time
from selenium.webdriver.common.keys import Keys

class RequestUpdSeleniumTest(LiveServerTestCase):
    
    
    def test_UploadDataPDInvalid(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/upload_dataPD/')
        time.sleep(2)
        
        file = driver.find_element(By.ID, 'id_file')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        file.send_keys('C:\\Users\\Darwin Lenis\\OneDrive\\Escritorio\\Universidad\\5to Semestre\\Proyecto Integrador\\GitHub\\Final-Project\\follow_students\\static\\excel_format\\FORMATO_SIS_CURSOS-NOTAS.xlsx')
        
        summit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'No se cargó ningún dato en la base de datos')

        driver.quit()
        
    def test_UploadDataPDValid(self):
        
        major =  Major.objects.create(
            name = "Ingenieria de Sistema",
            price = 12300000
        )
        
        Major.save(major)
        
        student = Student.objects.create(
            name = "Neymar Jr",
            phoneNumber = "1234567890",
            date = "2023-01-01",
            icfes = 0,
            cedula = "1234",
            code = "A00381657",
            mail = "neymar@example.com",
            major = major
        )
        
        Student.save(student)
        
        staticmethod
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/upload_dataPD/')
        time.sleep(2)
        
        file = driver.find_element(By.ID, 'id_file')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        file.send_keys('C:\\Users\\Darwin Lenis\\OneDrive\\Escritorio\\Universidad\\5to Semestre\\Proyecto Integrador\\GitHub\\Final-Project\\follow_students\\static\\excel_format\\FORMATO_SIS_CURSOS-NOTAS.xlsx')
        
        summit_button.click()
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Se cargó correctamente')

        driver.quit()
        

