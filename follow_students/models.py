from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
class Students(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    icfes = models.IntegerField()
    id_card = models.CharField(max_length=15)
    code = models.CharField(max_length=15)
    mail = models.EmailField()

    def __str__(self):
        return self.name