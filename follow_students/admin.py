from django.contrib import admin


# Register your models here.

from .models import Donante,Estudiante,Montos,User, Major, Beca, Curso, Nota

# Register your models here.
admin.site.register(User)
admin.site.register(Donante)
admin.site.register(Montos)
admin.site.register(Major)
admin.site.register(Beca)
admin.site.register(Estudiante)
admin.site.register(Nota)
admin.site.register(Curso)


