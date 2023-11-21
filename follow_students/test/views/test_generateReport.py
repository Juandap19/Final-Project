from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from follow_students.models import *
import time
import re

class RequestUpdSeleniumTest(LiveServerTestCase):
    def test_MenuReport(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/menuReport/')
        time.sleep(2)
        
        submit = driver.find_element(by=By.XPATH, value="//input[@type='search']")
        submit.send_keys('A00381293')

        time.sleep(2)

        checkbox = driver.find_element(By.NAME, 'selected_students')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        checkbox.click()
        summit_button.click()
        time.sleep(2)
        
        current_url = driver.current_url

        # Reemplaza el número de puerto en la URL actual con '8000'
        expected_url = re.sub(r'http://[^/]+:\d+', 'http://127.0.0.1:8000', current_url)

        # Verifica que la URL actual coincida con la URL esperada
        self.assertEqual(current_url, expected_url)

        driver.quit()
    
    def test_GenerateReport(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/menuReport/')
        time.sleep(2)

        submit = driver.find_element(by=By.XPATH, value="//input[@type='search']")
        submit.send_keys('A00381293')

        time.sleep(2)
        
        checkbox = driver.find_element(By.NAME, 'selected_students')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        checkbox.click()
        summit_button.click()
        time.sleep(2)
        
        pdf_button = driver.find_element(By.ID, 'pdf-button')
        
        pdf_button.click()
        driver.quit()
        
        
        

        
        