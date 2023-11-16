from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoalEvaluation(LiveServerTestCase):

    def test_GoalEvaluation(self):
        
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/studentManage/')
        time.sleep(2)
        
        old_url = driver.current_url

        submit_button = driver.find_element(By.ID, 'btn-goal')

        time.sleep(2)

        submit_button.click()
        time.sleep(2)

        current_url = driver.current_url

        self.assertNotEqual(current_url, old_url)
    
    def test_goal_evaluation_message(self):

        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/studentManage/goalEvaluation/1/')

        try:
            alert_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-warning'))
            )

            expected_text = "Este estudiante tiene una beca asociada, pero no hay metas asignadas."
            self.assertEqual(alert_element.text, expected_text)
        except TimeoutException:
            self.fail("Tiempo de espera agotado. Elemento no encontrado.")