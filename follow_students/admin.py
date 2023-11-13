from django.contrib import admin

from .models import Notification, User, Grade, Student, Course, Donor, Amount, Major,ScholarshipGoal,ScholarshipGoalAssociation, Scholarship, Consult, NonAcademicActivity,RegisNonAcademicActivity, Scholarship_expense, Rol, RolPermiso, Permiso


admin.site.register(User)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Donor)
admin.site.register(Amount)
admin.site.register(Major)
admin.site.register(ScholarshipGoal)
admin.site.register(ScholarshipGoalAssociation)
admin.site.register(Scholarship)
admin.site.register(Consult)
admin.site.register(NonAcademicActivity)
admin.site.register(RegisNonAcademicActivity)
admin.site.register(Scholarship_expense)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Permiso)
admin.site.register(Notification)
