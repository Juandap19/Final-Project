from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student,Grade,Notification
from follow_students.views.menuCancelation import MenuCancelation


class CancelationSection(View):
    ides=MenuCancelation.ides
    
    def get(self, request):
        gradesList=Grade.objects.all()
        idesTemp = self.ides.copy()
        self.ides.clear()
        return render(request, 'cancelationSection.html', {
            "grades" : gradesList,
            "ides": idesTemp
        })
        
    def post(self, request ,  code):
         grade= get_object_or_404(Grade,pk=code)
         if request.method == 'POST':
            grade.state=False
            grade.save()
        
            notification = Notification(name="Cancelacion de {}".format(grade.student.name), student=grade.student, description="{} Cancelo {}".format(grade.student.name, grade.course.code))
            notification.save()
            studentlist=Student.objects.all()
         return render(request, 'menuCancelation.html', {
            "students" : studentlist,
            "studentUpdate": True
        })
         
         