from django.test import TestCase
from django.urls import reverse
from follow_students.models import *
from follow_students.views.upload_dataBU import Upload_dataBU
from django.test import Client

class UploadDataBUViewTest(TestCase):
    def setUp(self):
        # Configura datos iniciales para las pruebas
        
        self.major =  Major.objects.create(
            name = "Ingenieria de Sistema",
            price = 12300000
        )
        
        self.student = Student.objects.create(
            name = "Leonel Messi",
            phoneNumber = "1234567890",
            date = "2023-01-01",
            icfes = 500,
            cedula = "1109114877",
            code = "A00381657",
            mail = "estudiante@example.com",
            major = self.major,
        )
        

    def test_upload_dataBU_GET(self):
        
        url = reverse('uploadBU')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'upload_dataBU.html') 

    def test_upload_dataBU_POST_valid_data(self):
        
        url = reverse('uploadBU')  
        form_data = {
            'student_code': 'A00381657',  
            'activity': 1,  
            'assistance_days': '5',
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(RegisNonAcademicActivity.objects.count(), 1)  

    def test_upload_dataBU_POST_invalid_data(self):
        
        url = reverse('uploadBU')  
        form_data = {
            'student_code': 'A00381242', 
            'activity': 1,  
            'assistance_days': '5',
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'upload_dataBU.html')  

    

