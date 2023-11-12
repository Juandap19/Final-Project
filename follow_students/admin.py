from django.contrib import admin

from .models import User, Nota, Student, Curso, Donor, Amount, Major,ScholarshipGoal,ScholarshipGoalAssociation, Scholarship, Consulta, ActividadNoAcademica,RegistroActividadEstudiante, Gasto_beca, Rol, RolPermiso, Permiso

admin.site.register(User)
admin.site.register(Nota)
admin.site.register(Student)
admin.site.register(Curso)
admin.site.register(Donor)
admin.site.register(Amount)
admin.site.register(Major)
admin.site.register(ScholarshipGoal)
admin.site.register(ScholarshipGoalAssociation)
admin.site.register(Scholarship)
admin.site.register(Consulta)
admin.site.register(ActividadNoAcademica)
admin.site.register(RegistroActividadEstudiante)
admin.site.register(Gasto_beca)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Permiso)
