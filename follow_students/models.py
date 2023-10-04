from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=255)
    celphone = models.CharField(max_length=15)
    date = models.DateField()
    icfes = models.IntegerField()
    cc = models.CharField(max_length=15)
    code = models.CharField(max_length=15)
    email = models.EmailField()


class Scholarship_Expenses(models.Model):
    student_code = models.CharField(max_length=20, unique=True)
    money_quantity = models.FloatField()
    acumulate_time = models.IntegerField()
    class Time_way(models.TextChoices):
        DAYS = "1", "Dias"
        MONTH = "2", "Mes"
        YEAR = "3", "Año"

    select_time = models.CharField(
        max_length = 2,
        choices = Time_way.choices,
        default = Time_way.DAYS 
    )

