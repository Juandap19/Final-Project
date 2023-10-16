from django.contrib import admin

from .models import User, Nota, Estudiante, Curso, Donante, Montos, Major, Beca, Consulta, ActividadNoAcademica,RegistroActividadEstudiante, Gasto_beca, Rol, RolPermiso, Permiso

admin.site.register(User)
admin.site.register(Nota)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Donante)
admin.site.register(Montos)
admin.site.register(Major)
admin.site.register(Beca)
admin.site.register(Consulta)
admin.site.register(ActividadNoAcademica)
admin.site.register(RegistroActividadEstudiante)
admin.site.register(Gasto_beca)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Permiso)