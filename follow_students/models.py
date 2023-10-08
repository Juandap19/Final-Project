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
    transporte = models.IntegerField()
    alimentacion = models.IntegerField()
    academico = models.IntegerField()

    def __str__(self):
         text ="{}".format(self.transporte)
         return text



 

class Beca(models.Model):
    code  = models.CharField(max_length=20, unique=True, primary_key=True)
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
    codigo = models.CharField(max_length=20, unique=True, primary_key=True)
    correo = models.EmailField()
    beca = models.ForeignKey(Beca, on_delete=models.SET_NULL, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    aux_transportation = models.CharField(max_length=100, unique= False , default=0)
    aux_academic = models.CharField(max_length=100, unique= False , default=0)
    
    def __str__(self):
        return self.nombre
      
class Gasto_beca(models.Model):
    estudiante = models.ForeignKey(Estudiante, null=True, on_delete= models.CASCADE, unique = False)
    beca = models.ForeignKey(Beca, null = True, on_delete= models.CASCADE, unique = False)
    cantidad_dinero = models.FloatField()
    tiempo_acumulado = models.IntegerField()
    class Time_way(models.TextChoices):
        DIAS = "1", "Dias"
        MES = "2", "Mes"
        ANIO = "3", "Año"

    tiempo_seleccionado = models.CharField(
        max_length = 2,
        choices = Time_way.choices,
        default = Time_way.DIAS 
    )
    tipo = models.CharField(max_length = 20, unique = False)

    def __str__(self):
        text = self.estudiante.codigo
        return text

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
        return self.estudiante.codigo

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


