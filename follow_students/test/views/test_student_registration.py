from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import re
from faker import Faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class StudentRegister(LiveServerTestCase):
    
    def test_StudentRegister(self):
        fake = Faker('es_CO')
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/studentsRegister/')
        time.sleep(2)
        
        name = driver.find_element(By.ID, 'name')
        phoneNumber = driver.find_element(By.ID, 'phoneNumber')
        date = driver.find_element(By.ID, 'date')
        icfes = driver.find_element(By.ID, 'icfes')
        id = driver.find_element(By.ID, 'cedula')
        code = driver.find_element(By.ID, 'code')
        mail = driver.find_element(By.ID, 'mail')
        major = driver.find_element(By.ID, 'major')
        submit_button = driver.find_element(By.ID, 'btn-register')
        name.send_keys('Dominic')
        phoneNumber.send_keys('3169443115')
        date.send_keys('11-10-2023')
        icfes.send_keys('500')
        id.send_keys(f'{fake.unique.random_number(digits=10)}')
        code.send_keys(f'A00{fake.unique.random_number(digits=6)}')
        mail.send_keys('Dominic1110417@gmail.com')
        select_major = Select(major)
        select_major.select_by_index(1)
        time.sleep(5)

        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        current_url = driver.current_url

        expected_url = re.sub(r'http://[^/]+:\d+', 'http://127.0.0.1:8000', current_url)

        self.assertEqual(current_url, expected_url)
    
    def test_AssignScholarship(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/assignScholarship/A00382231/')
        time.sleep(2)
        
        checkbox = driver.find_element(By.ID, 'scholarship_1')
        submit_button = driver.find_element(By.ID, 'btn-confirmar')
        time.sleep(2)

        checkbox_label = driver.find_element(By.CSS_SELECTOR, 'label[for="scholarship_1"]')
        checkbox_label.click()
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Beca asignada exitosamente')

        driver.quit()

    def test_SameID(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/studentsRegister/')
        time.sleep(2)
        
        name = driver.find_element(By.ID, 'name')
        phoneNumber = driver.find_element(By.ID, 'phoneNumber')
        date = driver.find_element(By.ID, 'date')
        icfes = driver.find_element(By.ID, 'icfes')
        id = driver.find_element(By.ID, 'cedula')
        code = driver.find_element(By.ID, 'code')
        mail = driver.find_element(By.ID, 'mail')
        major = driver.find_element(By.ID, 'major')
        submit_button = driver.find_element(By.ID, 'btn-register')
        name.send_keys('patiño')
        phoneNumber.send_keys('3169443115')
        date.send_keys('11-10-2023')
        icfes.send_keys('500')
        id.send_keys('1107835369')
        code.send_keys('A0123243')
        mail.send_keys('danielm110417@gmail.com')
        select_major = Select(major)
        select_major.select_by_index(1)
        time.sleep(5)

        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Ya existe un estudiante con esta cédula.')

    def test_SameCODE(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/studentsRegister/')
        time.sleep(2)
        
        name = driver.find_element(By.ID, 'name')
        phoneNumber = driver.find_element(By.ID, 'phoneNumber')
        date = driver.find_element(By.ID, 'date')
        icfes = driver.find_element(By.ID, 'icfes')
        id = driver.find_element(By.ID, 'cedula')
        code = driver.find_element(By.ID, 'code')
        mail = driver.find_element(By.ID, 'mail')
        major = driver.find_element(By.ID, 'major')
        submit_button = driver.find_element(By.ID, 'btn-register')
        name.send_keys('Daniel')
        phoneNumber.send_keys('3169443115')
        date.send_keys('11-10-2023')
        icfes.send_keys('500')
        id.send_keys('9999999994')
        code.send_keys('A00381293')
        mail.send_keys('danielm110417@gmail.com')
        select_major = Select(major)
        select_major.select_by_index(1)
        time.sleep(5)

        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Ya existe un estudiante con este código.')

    def test_NoScholarshipSelected(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/assignScholarship/A00382231/')
        time.sleep(2  )
        
        checkbox = driver.find_element(By.ID, 'scholarship_1')
        submit_button = driver.find_element(By.ID, 'btn-confirmar')
        time.sleep(2)

        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Por favor, seleccione una beca antes de continuar.')

        driver.quit()


    
