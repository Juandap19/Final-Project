import io
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from follow_students.forms.upload_dataPD_form import UploadFileForm
from follow_students.views.upload_dataPD import Upload_dataPD
from follow_students.models import Grade, Student, Course
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import pandas as pd  # Importa pandas para la lectura de archivos Excel

class UploadDataPDViewTest(TestCase):
    def test_upload_dataPD_GET(self):
        response = self.client.get(reverse('uploadPD'))
        self.assertEqual(response.status_code, 200)  # Verifica que la vista se cargue correctamente
        self.assertTemplateUsed(response, 'upload_dataPD.html')  # Verifica que se use la plantilla adecuada

    def test_upload_dataPD_POST_valid_data(self):
        # Crea un archivo de prueba en memoria
        file_content = (
            b'Codigo,NotaCurso\n123ABC,95.5\n456DEF,88.0\n'
        )
        file_content = b'Content of the file goes here.'
        file = SimpleUploadedFile('grades.xlsx', file_content, content_type='application/vnd.ms-excel')

        data = {
            'file': file,
        }
        response = self.client.post(reverse('uploadPD'), data, format='multipart')
        self.assertEqual(response.status_code, 302)  # Verifica que la redirección sea exitosa
        
        # Asegúrate de que los datos se hayan procesado correctamente en la base de datos
        self.assertEqual(Grade.objects.count(), 2)
        self.assertEqual(Grade.objects.get(student__code='123ABC').grade, 95.5)
        self.assertEqual(Grade.objects.get(student__code='456DEF').grade, 88.0)

    def test_upload_dataPD_POST_empty_data(self):
        data = {}
        response = self.client.post(reverse('uploadPD'), data, format='multipart')
        self.assertEqual(response.status_code, 200)  # Verifica que la vista muestre errores
        self.assertFormError(response, 'form', 'file', 'Este campo es obligatorio.')

    def test_upload_dataPD_POST_invalid_file(self):
        # Crea un archivo inválido (por ejemplo, un archivo de texto en lugar de un archivo Excel)
        file_content = f'Archivo de texto no válido'
        file = SimpleUploadedFile('invalid_file.txt', file_content, content_type='text/plain')
        
        data = {
            'file': file,
        }
        response = self.client.post(reverse('uploadPD'), data, format='multipart')
        self.assertEqual(response.status_code, 302)  # Verifica la redirección
        # Verifica que se muestre un mensaje de error
        self.assertContains(response, 'Hubo un error al cargar el archivo')

