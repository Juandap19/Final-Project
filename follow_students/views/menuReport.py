
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Estudiante




class MenuReport (View):

    
    def get(self, request):
        studentlist=Estudiante.objects.all()
        return render(request, 'menuReport.html', {
            "students" : studentlist
        })
    
 