from django.test import TestCase, Client
from django.urls import reverse
from follow_students.models import *

class Academic_TransportTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Client = Client()

        cls.the_donor = Donor.objects.create(cedula = "1107835369" , name = "Juan David Patiño" , mail = "juanda232405@hotmail.com", description = "Joven empresario, ganadero, panadero, futuro dueño de Icesi" )

        cls.amount1 = Amount.objects.create(code = '199' , transport = 10000000 , alimentation = 5000000 , academic =  50000000 )

        cls.amount2 = Amount.objects.create(code = '299' , transport = 6000000 , alimentation = 2000000 , academic =  1200000 )

        cls.scholarship1 = Scholarship.objects.create(code = "099" , name = "Emcali" ,amount = cls.amount1, donor = cls.the_donor, assigned_students =  1 , academic_percentage = 50 , transportation = 300000, image = "logo_EMCALI.png")

        cls.scholarship2 = Scholarship.objects.create(code = "098" , name = "Valle Del lili" ,amount = cls.amount2, donor = cls.the_donor, assigned_students =  1 , academic_percentage = 100 , transportation = 100000, image = "logo_FUNDACION.png")


        # Crear una carrera (Major)
        cls.major = Major.objects.create(
            name="Ingeniería de Sistemas",
            price=10300000
        )

        # Crear un estudiante (Student)
        cls.student = Student.objects.create(
            name="Juan Carmelo",
            phoneNumber="12367890",
            date="2023-01-01",
            icfes=0,
            cedula="1234",
            code="A00381289",
            mail="juanda2342324@example.com",
            major=cls.major,
            scholarship = cls.scholarship1
        )

        # Crear una carrera (Major)
        cls.major2 = Major.objects.create(
            name="Pedagogia",
            price=7300000
        )

        # Crear un estudiante (Student)
        cls.student2 = Student.objects.create(
            name="Juan Carlos Alberto",
            phoneNumber="12347810",
            date="2023-02-01",
            icfes=0,
            cedula="12343",
            code="A00381299",
            mail="juaAlbero324@example.com",
            major=cls.major2,
            scholarship = cls.scholarship2
        )

    def test_get_render_page_Academic(self):
        response = self.client.get('/apoyo_financiero_academico/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './financial_education_transportation.html')
        
    def test_get_render_page_Transport(self):
        response = self.client.get('/apoyo_financiero_transporte/')            
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './financial_education_transportation.html')


    def test_post_success_academic(self):
        response = self.client.post('/apoyo_financiero_academico/', {
            'student_code': self.student.code,
            })
        estudiante_gasto = Scholarship_expense.objects.get(student = self.student)
        self.assertEqual(self.student.code,estudiante_gasto.student.code)


    def test_post_already_paid_academic(self):
        the_student = self.student
        the_student.aux_academic = "1"
        the_student.save()

        gastos_antes = Scholarship_expense.objects.count()
        response = self.client.post('/apoyo_financiero_Transporte/', {
            'student_code': self.student.code,
            })
        
        self.assertEqual(gastos_antes, Scholarship_expense.objects.count())

    
    def test_post_not_exist_id_academic(self):
        gastos_antes = Scholarship_expense.objects.count()
        response = self.client.post('/apoyo_financiero_Transporte/', {
            'student_code': "no existe",
            })
        
        self.assertEqual(gastos_antes, Scholarship_expense.objects.count())
