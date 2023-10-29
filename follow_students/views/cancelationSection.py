from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student,Nota
from follow_students.views.menuCancelation import MenuCancelation


class CancelationSection(View):
    ides=MenuCancelation.ides
    
    def get(self, request):
        gradesList=Nota.objects.all()
        idesTemp = self.ides.copy()
        self.ides.clear()
        return render(request, 'cancelationSection.html', {
            "grades" : gradesList,
            "ides": idesTemp
        })
        
