from django.db import models

# Create your models here.

class Crea(models.Model):
    hora = models.CharField(max_length = 100)
    motivo = models.CharField(max_length = 200)
    resultado = models.CharField(max_length = 200)

