from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Students

class StudentEdit(View):

    def get(self, request, pk):
     
        student_to_edit = get_object_or_404(Students, id = pk)
        return render(request, 'studentEdit.html', {
            'student': student_to_edit
        })
    
    def post(self, request, *args, **kwargs):

        id = int(request.POST['idStudent'])

        student_to_edit = Students.objects.get(pk = id)

        student_to_edit.code = request.POST['code']
        student_to_edit.name = request.POST['name']
        student_to_edit.id_card = request.POST['id_card']
        student_to_edit.phone_number = request.POST['phone_number']
        date_str = request.POST['birthday']
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        student_to_edit.date = date_obj
        student_to_edit.icfes = request.POST['icfes']
        student_to_edit.mail = request.POST['mail']

        student_to_edit.save()

        return render(request, 'studentEdit.html', {
            "student": student_to_edit,
            "studentUpdate": True
        })