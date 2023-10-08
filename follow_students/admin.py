from django.contrib import admin
from .models import Donante,Estudiante,Montos,User, Major, Beca

# Register your models here.
admin.site.register(User)
admin.site.register(Donante)
admin.site.register(Montos)
admin.site.register(Major)
admin.site.register(Beca)
admin.site.register(Estudiante)

