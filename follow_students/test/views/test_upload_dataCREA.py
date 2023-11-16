from django.test import TestCase
from django.urls import reverse
from follow_students.models import *
from follow_students.views.upload_dataCREA import RegisConsult
from django.test import Client

class UploadDataCREAViewTest(TestCase):
    def setUp(self):
        
        self.major =  Major.objects.create(
            name = "Ingenieria de Sistema",
            price = 12300000
        )
        
        self.student = Student.objects.create(
            name = "Neymar Jr",
            phoneNumber = "1234567890",
            date = "2023-01-01",
            icfes = 0,
            cedula = "1234",
            code = "A00381242",
            mail = "neymar@example.com",
            major = self.major,
        )
        
        self.support_center = SupportCenter.objects.create(name="Centro Leo")

    def test_RegisConsultForm_valid_data(self):
        # Prueba el formulario con datos válidos
        data = {
            'student_code': 'A00381242',  
            'support_center': self.support_center.id,  
            'date': '2023-01-01',
            'time': '12:00:00',
            'reason': 'Razón de la consulta',
            'outcome': 'Resultado de la consulta',
        }
        form = RegisConsult(data=data)
        self.assertTrue(form.is_valid())  # El formulario debe ser válido

    def test_RegisConsultForm_empty_data(self):
       
        data = {}
        form = RegisConsult(data=data)
        self.assertFalse(form.is_valid())  # El formulario no debe ser válido

    def test_RegisConsultForm_invalid_data(self):
        
        data = {
            'student_code': 'A00381242',  
            'support_center': 'Centro No Existente',  
            'date': 'Fecha No Válida',  
            'time': 'Hora Inválida',  
            'reason': '', 
            'outcome': '',  
        }
        form = RegisConsult(data=data)
        self.assertFalse(form.is_valid())  # El formulario no debe ser válido