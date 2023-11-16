from django.test import TestCase, Client
from django.urls import reverse
from follow_students.models import *

class NotificationsTests(TestCase):
    def setUp(self):
        self.client = Client()
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
        
    def test_get_notifications(self):
        response = self.client.get(reverse('notis'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notification.html')
        self.assertContains(response, 'NOTIFICACIONES')

    def test_post_clear_notifications(self):
        # Crear una notificación para verificar que se borre
        notification = Notification.objects.create(
            name='Test Notification',
            student=self.student,  # Ajusta esto según tus modelos
            description='Test Description',
            state=True
        )

        response = self.client.post(reverse('clean'))
        self.assertEqual(response.status_code, 302)  # 302 es el código de redirección después de la eliminación

        # Recargar la notificación desde la base de datos
        updated_notification = Notification.objects.get(pk=notification.pk)
        self.assertFalse(updated_notification.state)  # Verifica que el estado se haya actualizado a False
