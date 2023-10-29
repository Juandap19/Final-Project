from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student,Nota




class GenerateReport(View):
    ides=[]
    
    def get(self, request):
        gradesList=Nota.objects.all()
        idesTemp = self.ides.copy()
        self.ides.clear()
        return render(request, 'generateReport.html', {
            "grades" : gradesList,
            "ides": idesTemp
        })
        
    def post(self, request ,  code):
         student = get_object_or_404(Student, pk=code)
         if student not in self.ides:
            self.ides.append(student)
            
         return redirect("/menuReport")