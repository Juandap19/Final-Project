from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

class Estudiante(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ActividadNoAcademica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class RegistroActividadEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    actividad = models.ForeignKey(ActividadNoAcademica, on_delete=models.CASCADE)
    dias_asistencia = models.CharField(max_length=100)

    def __str__(self):
        return f'Registro de {self.estudiante.nombre} en {self.actividad.nombre}'


