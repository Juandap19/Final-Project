from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Students

class StudentManage(View):

    def get(self, request):

        students = Students.objects.all()
        return render(request, 'studentManage.html', {
            'students': students
            })
    
    def post(self, request, *args, **kwargs):

        eliminate_student = Students.objects.get(id = request.POST['idStudent'])
        eliminate_student.delete()

        return redirect('studentManage')