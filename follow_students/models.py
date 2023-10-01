from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    fecha = models.DateField()
    icfes = models.IntegerField()
    cedula = models.CharField(max_length=15)
    codigo = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre