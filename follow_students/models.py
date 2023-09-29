from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
class DataDP(models.Model):
    code = models.CharField(max_length=100)
    grade1 = models.FloatField()
    grade2 = models.FloatField()
    grade3 = models.FloatField()
    
    def __str__(self):
        return self.Numero_de_ID