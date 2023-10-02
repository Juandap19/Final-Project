from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
    
class Curso(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Estudiante(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Nota(models.Model):
    grade = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.estudiante.name
