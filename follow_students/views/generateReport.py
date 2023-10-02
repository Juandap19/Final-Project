
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Estudiante,Curso,Nota




class GenerateReport(View):
    ides=[]
    
    def get(self, request):
        gradesList=Nota.objects.all()
        return render(request, 'generateReport.html', {
            "grades" : gradesList,
            "ides": self.ides
        })
        
    def post(self, request ,  codigo):
         student = get_object_or_404(Estudiante, pk=codigo)
         self.ides.append(student)
         return redirect("/menuReport")