from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student, Consulta, Nota

class GenerateReport(View):
    ides = []

    def get(self, request):
        consultaList = Consulta.objects.all()
        gradesList = Nota.objects.all()
        
        idesTemp = self.ides.copy()
        self.ides.clear()

        return render(request, 'generateReport.html', {
            "consultas": consultaList,
            "grades": gradesList,
            "ides": idesTemp
        })

    def post(self, request, code):
        student = get_object_or_404(Student, pk=code)
        if student not in self.ides:
            self.ides.append(student)
        return redirect("/menuReport")  # Ajusta la URL según tu configuración