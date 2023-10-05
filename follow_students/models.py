from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
    
class Donor(models.Model):
    code = models.CharField(max_length = 15, primary_key=True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 15)
    description = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        text = "{0} {1}"
        return text.format(self.code, self.name)
    

class Scholarship_Funds(models.Model):
    code_id = models.CharField(max_length=20,primary_key=True)    
    alimentation_fund = models.FloatField()
    tranportation_fund = models.FloatField()
    education_fund = models.FloatField()

    def __str__(self):
        text = "{0} {1} {2} {3}"
        return text.format(self.code_id, self.alimentation_fund, self.tranportation_fund , self.education_fund)


class Scholarship(models.Model):
    code = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=15)
    donor = models.ForeignKey(Donor, null=True, on_delete= models.CASCADE)
    code_Funds =  models.ForeignKey(Scholarship_Funds, null=True, on_delete= models.CASCADE)

    def __str__(self):
        text = "{0} {1} {2}"
        return text.format(self.code, self.name, self.code)


class Student(models.Model):
    code = models.CharField(max_length=15, primary_key=True )
    name = models.CharField(max_length=255)
    celphone = models.CharField(max_length=15)
    date = models.DateField()
    icfes = models.IntegerField()
    cc = models.CharField(max_length=15)
    email = models.EmailField()
    scholarship_id = models.ForeignKey(Scholarship, null=True, on_delete= models.CASCADE)

    def __str__(self):
        text = "{0} {1} {2}"
        return text.format(self.code, self.name, self.scholarship_id)
    
    

class Scholarship_Expenses(models.Model):
    code = models.CharField(max_length = 20, unique = False, primary_key = True)
    student_code = models.CharField(max_length = 20, unique = False)
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

    def __str__(self):
        return self.student_code
