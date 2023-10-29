from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_permiso

class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE) 

    def __str__(self):
        return self.username

class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

class Curso(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.code
      
class Major(models.Model):
    name = models.CharField(max_length=255)
    price= models.IntegerField()

    def __str__(self):
        return self.name

class Donor(models.Model):
    cedula = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Amount(models.Model):
    code = models.CharField(max_length=20, unique=True, default = "23")
    transporte = models.IntegerField()
    alimentacion = models.IntegerField()
    academico = models.IntegerField()

    def __str__(self):
         text ="{}".format(self.code)
         return text

class Scholarship(models.Model):
    code  = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    assigned_students = models.PositiveIntegerField(default=0)
    porcentaje_academico = models.IntegerField(default = 70)
    auxilio_transporte = models.IntegerField(default = 1000000)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    date = models.DateField()
    icfes = models.IntegerField()
    cedula = models.CharField(max_length=20)
    code = models.CharField(max_length=20, unique=True)
    mail = models.EmailField()
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    aux_transportation = models.CharField(max_length=100, unique= False , default=0)
    aux_academic = models.CharField(max_length=100, unique= False , default=0)
    
    def __str__(self):
        return self.name
      
class Gasto_beca(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete= models.CASCADE, unique = False)
    scholarship = models.ForeignKey(Scholarship, null = True, on_delete= models.CASCADE, unique = False)
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
        text = self.student.code
        return text

class Consulta(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    resultado = models.TextField()
    
    def __str__(self):
        return f'Consulta realizada por {self.student.name} el {self.fecha}'

class Nota(models.Model):
    grade = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.code

class ActividadNoAcademica(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
      
class RegistroActividadEstudiante(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    actividad = models.ForeignKey(ActividadNoAcademica, on_delete=models.CASCADE)
    dias_asistencia = models.CharField(max_length=100)

    def __str__(self):
        return f'Registro de {self.student.nombre} en {self.actividad.nombre}'


