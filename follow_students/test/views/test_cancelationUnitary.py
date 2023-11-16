from django.test import TestCase, Client
from django.urls import reverse
from follow_students.models import *

class CancelationSectionTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear una carrera (Major)
        self.major = Major.objects.create(
            name="Ingeniería de Sistemas",
            price=12300000
        )

        # Crear un estudiante (Student)
        self.student = Student.objects.create(
            name="Neymar Jr",
            phoneNumber="1234567890",
            date="2023-01-01",
            icfes=0,
            cedula="1234",
            code="A00381242",
            mail="neymar@example.com",
            major=self.major
        )

        # Crear un curso (Course)
        self.course = Course.objects.create(code="123", name="juan")

        # Crear una calificación (Grade) asociada al estudiante y curso
        self.grade = Grade.objects.create(grade=2, student=self.student, course=self.course, state=True)

    def test_post_cancelation_course(self):
        # Crear una nueva calificación independiente para la segunda prueba
        grade = Grade.objects.create(grade=3, student=self.student, course=self.course, state=True)

        url = reverse('cancelation', kwargs={'code': grade.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuCancelation.html')

        # Recargar el objeto desde la base de datos para obtener el estado más reciente
        updated_grade = Grade.objects.get(pk=grade.id)
        self.assertFalse(updated_grade.state)
