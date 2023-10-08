from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Estudiante

class StudentManage(View):

    def get(self, request):

        students = Estudiante.objects.all()
        return render(request, 'studentManage.html', {
            'students': students
            })
    
    def post(self, request, *args, **kwargs):

        eliminate_student = Estudiante.objects.get(id = request.POST['idStudent'])
        eliminate_student.delete()

        return redirect('studentManage')