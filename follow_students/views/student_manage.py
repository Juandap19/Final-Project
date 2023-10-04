from django.views import View
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Students

class StudentManage(View):

    def get(self, request):
        students = Students.objects.all()
        return render(request, 'studentManage.html', {
            'students': students
            })
    
    def post(self, request):

        return