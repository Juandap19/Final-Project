from django.contrib import admin
from .models import Nota,Estudiante,Curso,User

# Register your models here.

admin.site.register(User)
admin.site.register(Nota)
admin.site.register(Estudiante)
admin.site.register(Curso)