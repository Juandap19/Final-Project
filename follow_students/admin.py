from django.contrib import admin
from .models import User, Scholarship_Expense, Student, Scholarship, Donor , Scholarship_Fund, Major

# Register your models here.
admin.site.register(User)
admin.site.register(Scholarship_Expense)
admin.site.register(Student)
admin.site.register(Donor)
admin.site.register(Scholarship)
admin.site.register(Scholarship_Fund)
admin.site.register(Major)