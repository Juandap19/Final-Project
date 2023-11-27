from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from follow_students.models import Student, Consult, Grade, RegisNonAcademicActivity, Scholarship_expense
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

class GeneratePDF(View):
    def get(self, request, code):
        
        student = get_object_or_404(Student, pk=code)
        consultaList = Consult.objects.filter(student=student)
        gradesList = Grade.objects.filter(student=student)
        bu = RegisNonAcademicActivity.objects.filter(student=student)
        expenses = Scholarship_expense.objects.filter(student=student)

        if gradesList:
            total_grades = sum(grade.grade for grade in gradesList)
            average_grade = total_grades / len(gradesList)
        else:
            average_grade = 0.0

        template = get_template('pdf_template.html')
        context = {
            'student': student,
            'gradesList': gradesList,
            'consultaList': consultaList,
            'bu': bu,
            "expenses": expenses,
            'avg': round(average_grade, 2)
        }
        content = template.render(context)

        html_with_image = f'<img src="follow_students/static/images/logo_ICESI.png" alt="Descripción de la imagen">' + content

        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html_with_image.encode("UTF-8")), result)

        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            filename = f'reporte_{student.code}.pdf'
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        else:
            return HttpResponse(f'Error al generar el PDF para el estudiante {student}: {pdf.err}')
