from django.contrib import admin
from follow_students.models import Consulta, Estudiante

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Consulta)