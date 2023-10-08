from django.contrib import admin
from .models import User, Gasto_beca, Estudiante, Beca, Donante , Monto, Major

# Register your models here.
admin.site.register(User)
admin.site.register(Gasto_beca)
admin.site.register(Estudiante)
admin.site.register(Donante)
admin.site.register(Beca)
admin.site.register(Monto)
admin.site.register(Major)