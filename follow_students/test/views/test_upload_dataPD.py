from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from follow_students.models import *
import time
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from follow_students.models import *
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

class RequestUpdSeleniumTest(LiveServerTestCase):
    
    
    def test_UploadDataPDInvalid(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/upload_dataPD/')
        time.sleep(2)
        
        file = driver.find_element(By.ID, 'id_file')
        summit_button = driver.find_element(By.ID, 'send-button')
        
        current_file_path = Path(__file__).parent.parent.parent.parent
        relative_file_path = current_file_path.joinpath("follow_students", "static", "excel_format", "FORMATO_SIS_CURSOS-NOTAS.xlsx")
        
        file.send_keys(str(relative_file_path))
        
        summit_button.send_keys(Keys.RETURN)
        time.sleep(2)
        
        sweet_alert = driver.find_element(By.ID, 'swal2-title')
        sweet_alert_text = sweet_alert.text
        self.assertEquals(sweet_alert_text, 'Se cargó correctamente')

        driver.quit()
        
