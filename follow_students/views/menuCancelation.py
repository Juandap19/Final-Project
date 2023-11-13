
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student




class MenuCancelation(View):
    ides=[]
    
    def get(self, request):
        studentlist=Student.objects.all()
        return render(request, 'menuCancelation.html', {
            "students" : studentlist
        })
    
    def post(self, request ,  code):
         student = get_object_or_404(Student, pk=code)
         if student not in self.ides:
            self.ides.append(student)
            
         return redirect("/cancelationSection")