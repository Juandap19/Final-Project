from django.contrib import admin

from .models import User, Grade, Student, Course, Donor, Amount, Major, Scholarship, Consult, NonAcademicActivity,RegisNonAcademicActivity, Gasto_beca, Rol, RolPermiso, Permiso

admin.site.register(User)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Donor)
admin.site.register(Amount)
admin.site.register(Major)
admin.site.register(Scholarship)
admin.site.register(Consult)
admin.site.register(NonAcademicActivity)
admin.site.register(RegisNonAcademicActivity)
admin.site.register(Gasto_beca)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Permiso)