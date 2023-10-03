from django.contrib import admin
from .models import ActividadNoAcademica,RegistroActividadEstudiante,Estudiante

# Register your models here.

admin.site.register(ActividadNoAcademica)
admin.site.register(RegistroActividadEstudiante)
admin.site.register(Estudiante)
