from django.views import View
from django.shortcuts import render
from follow_students.models import Student, Scholarship, Donor, Notification

class Dashboard(View):
    def get(self, request):

        students = Student.objects.all()
        scholarship = Scholarship.objects.all()
        donor = Donor.objects.all()
        noti = Notification.objects.filter(state=True)
        becas_seleccionadas = Scholarship.objects.all().order_by('-assigned_students')[:5]

        return render(request, 'dashboard.html', {
            'num_students': students.count(),
            'num_scholarship': scholarship.count(),
            'num_donor': donor.count(),
            'num_noti': noti.count(),
            'students': students,
            'scholarships': scholarship,
            'donors': donor,
            'notifications': noti,
            'becas': becas_seleccionadas,
        })