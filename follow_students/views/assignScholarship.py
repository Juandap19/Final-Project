from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from follow_students.forms.studentsRegister_form import StudentForm
from follow_students.models import Student, Scholarship
from django.contrib import messages
from django.http import HttpResponseRedirect

class AssignScholarship(View):
    def get(self, request, code):
        student = get_object_or_404(Student, code=code)
        title = "Django Course!!"
        form = StudentForm()
        scholarships = Scholarship.objects.all()
        return render(request, 'assignScholarship.html', {'title': title, 'form': form, 'mensaje': None, 'scholarships': scholarships, 'code': code, 'student': student})
    
    def post(self, request, code):
        scholarships = Scholarship.objects.all()
        student = get_object_or_404(Student, code=code)
        form = StudentForm(request.POST)

        if form.is_valid():
            # Obtener el ID de la beca seleccionada (si se proporcionó)
            scholarship_id = request.POST.get('scholarship_id')

            # Verificar si se ha seleccionado una beca
            if scholarship_id:
                nueva_scholarship = get_object_or_404(Scholarship, id=scholarship_id)

                # Disminuir el contador de estudiantes asignados en la beca anterior (si tenía una beca previa)
                if student.scholarship:
                    student.scholarship.assigned_students -= 1
                    student.scholarship.save()

                # Aumentar el contador de estudiantes asignados en la nueva beca
                nueva_scholarship.assigned_students += 1
                nueva_scholarship.save()

                # Asignar la nueva beca al estudiante
                student.scholarship = nueva_scholarship
                student.save()

                messages.success(request, "Beca asignada exitosamente")
                return redirect('asignar_scholarship', code=code)
            else:
                messages.error(request, "Por favor, seleccione una beca antes de continuar.")
        else:
            messages.error(request, "El formulario no es válido. Por favor, complete todos los campos.")

        return render(request, 'assignScholarship.html', {'scholarships': scholarships, 'form': form, 'code': code, 'student': student})
