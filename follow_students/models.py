from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
class Donante(models.Model):
    cedula = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class Monto(models.Model):
    transporte = models.IntegerField()
    alimentacion = models.IntegerField()
    academico = models.IntegerField()

    def __str__(self):
        text = "{0}"
        return text.format(self.id)

class Beca(models.Model):
    code = models.CharField(max_length=15,primary_key=True)
    nombre = models.CharField(max_length=255)
    montos = models.ForeignKey(Monto, on_delete=models.CASCADE)
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)

    def __str__(self):
        text = "{0} {1} "
        return text.format(self.code, self.nombre)
    

# Major.Major_code debe de ser Major.id
class Major(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()

    def __str__(self):
        text = "{0} {1} "
        return text.format( self.nombre, self.precio)


class Estudiante(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True )
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    fecha = models.DateField()
    icfes = models.IntegerField()
    cedula = models.CharField(max_length=15)
    correo = models.EmailField()
    beca = models.ForeignKey(Beca, null=True, on_delete= models.CASCADE)
    major = models.ForeignKey(Major, null=True, on_delete= models.CASCADE)
    aux_transportation = models.IntegerField(default = 0)
    aux_academic = models.IntegerField(default = 0)

    def __str__(self):
        text = "{0} {1} {2}"
        return text.format(self.codigo, self.nombre, self.beca_id)
    
    

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

