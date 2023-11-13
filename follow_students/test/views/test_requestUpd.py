from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class RequestUpdSeleniumTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Utiliza el controlador adecuado para tu navegador
        self.browser.implicitly_wait(3)  # Espera hasta 3 segundos para que los elementos carguen

    def tearDown(self):
        self.browser.quit()

    def test_request_update_form_submission(self):
        # Abre la página con el formulario
        self.browser.get(self.live_server_url + 'requestUpdate')

        # Encuentra los elementos del formulario
        destinatario_input = self.browser.find_element(By.NAME, 'destinatario')
        asunto_input = self.browser.find_element(By.NAME, 'asunto')
        mensaje_input = self.browser.find_element(By.NAME, 'mensaje')
        archivo_input = self.browser.find_element(By.NAME, 'archivo')
        submit_button = self.browser.find_element(By.ID, 'submit-button')

        # Ingresa información en los campos del formulario
        destinatario_input.send_keys('ejemplo@example.com')
        asunto_input.send_keys('Asunto de prueba')
        mensaje_input.send_keys('Este es un mensaje de prueba.')

        # Adjunta un archivo (si deseas probarlo)
        archivo_input.send_keys('/ruta/al/archivo.txt')

        # Envía el formulario haciendo clic en el botón de envío
        submit_button.click()

        # Espera un momento para que el correo se envíe
        self.browser.implicitly_wait(10)

        # Verifica que el formulario fue procesado correctamente
        success_message = self.browser.find_element(By.ID, 'success-message')
        self.assertEqual(success_message.text, 'Se ha enviado correctamente')

        # Puedes agregar más aserciones para verificar otras cosas si es necesario

        # Ejemplo: Verifica que la página se redirija a la misma página
        self.assertEqual(self.browser.current_url, self.live_server_url + '/ruta-a-tu-vista-request-upd')

    # Añade más pruebas según sea necesario
