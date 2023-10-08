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
      
class Major(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Donante(models.Model):
    cedula = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Montos(models.Model):
    code = models.CharField(max_length=100)
    transporte = models.IntegerField()
    alimentacion = models.IntegerField()
    academico = models.IntegerField()

    def __str__(self):
        return self.code

class Beca(models.Model):
    nombre = models.CharField(max_length=255)
    montos = models.ForeignKey(Montos, on_delete=models.CASCADE)
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)
    estudiantes_asignados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    fecha = models.DateField()
    icfes = models.IntegerField()
    cedula = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    beca = models.ForeignKey(Beca, on_delete=models.SET_NULL, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
      
class Consulta(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    resultado = models.TextField()
    
    def __str__(self):
        return f'Consulta realizada por {self.estudiante.nombre} el {self.fecha}'

class Nota(models.Model):
    grade = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.estudiante.code


