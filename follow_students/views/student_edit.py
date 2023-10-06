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

        return redirect(request, 'studentManage.html')