from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from follow_students.models import Student, Consulta, Nota, RegistroActividadEstudiante, Gasto_beca
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

class GeneratePDF(View):
    def get(self, request, code):
        
        student = get_object_or_404(Student, pk=code)
        consultaList = Consulta.objects.filter(student=student)
        gradesList = Nota.objects.filter(student=student)
        bu = RegistroActividadEstudiante.objects.filter(student=student)
        expenses = Gasto_beca.objects.filter(student=student)

        template = get_template('pdf_template.html')
        context = {
            'student': student,
            'gradesList': gradesList,
            'consultaList': consultaList,
            'bu': bu,
            "expenses": expenses,
        }
        content = template.render(context)

        html_with_image = f'<img src="follow_students/static/images/logo_ICESI.png" alt="Descripción de la imagen">' + content

        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html_with_image.encode("ISO-8859-1")), result)

        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            filename = f'reporte_{student.code}.pdf'
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        else:
            return HttpResponse(f'Error al generar el PDF para el estudiante {student}: {pdf.err}')
