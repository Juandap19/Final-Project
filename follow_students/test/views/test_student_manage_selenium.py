import random
from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

class testSeleniumStudentManage(LiveServerTestCase):

    def testEditStudent(self):

        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/studentManage/')
        time.sleep(2)

        elemento_h3 = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/h3")
        contenido_actual = elemento_h3.text
        contenido_esperado = "GESTIONAR ESTUDIANTE"
        self.assertEqual(contenido_actual, contenido_esperado)

        button_xpath = '/html/body/main/div[2]/article/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/button[1]'
        submit_button = driver.find_element(By.XPATH, button_xpath)
        submit_button.click()

        time.sleep(2)

        elemento_h3 = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/h3")
        contenido_actual = elemento_h3.text
        contenido_esperado = "EDITAR ESTUDIANTE"
        self.assertEqual(contenido_actual, contenido_esperado)

        input_icfes = driver.find_element(By.ID, 'icfes')
        input_icfes.clear() 
        new_score = random.randint(280, 500)
        input_icfes.send_keys(new_score) 

        btn_update = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/div/form/div[5]/button")
        btn_update.click()

        # time.sleep(5)

        # input_icfes_new = driver.find_element(By.ID, 'icfes')
        # print(input_icfes_new.text)
        # icfes_text = input_icfes_new.text
        # self.assertEqual(icfes_text, new_score)

        driver.quit()

    def testDeleteStudent(self):

        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/studentManage/')
        time.sleep(2)

        elemento_h3 = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/h3")
        contenido_actual = elemento_h3.text
        contenido_esperado = "GESTIONAR ESTUDIANTE"
        self.assertEqual(contenido_actual, contenido_esperado)

        time.sleep(2)

        btn_delete = driver.find_element(By.XPATH, "/html/body/main/div[2]/article/div/div/div/div[2]/div/table/tbody/tr[2]/td[9]/div/button[2]")
        btn_delete.click()

        time.sleep(2)

        btn_confirm = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
        btn_confirm.click()

        time.sleep(2)

        msg_confirm = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]").text
        self.assertEqual(msg_confirm, "El estudiante fue eliminado.")

        driver.quit()