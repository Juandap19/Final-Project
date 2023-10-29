
from django.shortcuts import render
from django.views import View
from follow_students.models import Student




class MenuCancelation(View):

    
    def get(self, request):
        studentlist=Student.objects.all()
        return render(request, 'menuCancelation.html', {
            "students" : studentlist
        })
    
 