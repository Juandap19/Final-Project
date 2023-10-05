from django.contrib import admin
from .models import User, Scholarship_Expenses, Student, Scholarship, Donor , Scholarship_Funds

# Register your models here.
admin.site.register(User)
admin.site.register(Scholarship_Expenses)
admin.site.register(Student)
admin.site.register(Donor)
admin.site.register(Scholarship)
admin.site.register(Scholarship_Funds)