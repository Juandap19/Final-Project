from django.contrib import admin
from .models import User, Nota, Estudiante, Curso, Donante, Montos, Major, Beca


# Register your models here.

admin.site.register(User)
admin.site.register(Nota)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Donante)
admin.site.register(Montos)
admin.site.register(Major)
admin.site.register(Beca)