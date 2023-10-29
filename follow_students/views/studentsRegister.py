from django.views import View
from django.shortcuts import render, redirect
from follow_students.forms.studentsRegister_form import StudentForm
from follow_students.models import Student, Major  
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.utils import IntegrityError 


class StudentsRegister(View):
    def get(self, request):
        title = "Django Course!!"
        majors = Major.objects.all()
        form = StudentForm()
        return render(request, 'studentsRegister.html', {'title': title,'majors':majors, 'form': form, 'mensaje': None})

    def post(self, request):
        majors = Major.objects.all()
        form = StudentForm(request.POST)

        if form.is_valid():
            # Extrae los datos del formulario
            name = form.cleaned_data['name']
            phoneNumber = form.cleaned_data['phoneNumber']
            date = form.cleaned_data['date']
            icfes = form.cleaned_data['icfes']
            cedula = form.cleaned_data['cedula']
            code = form.cleaned_data['code']
            mail = form.cleaned_data['mail']
            major_id = form.cleaned_data['major']
            major_instance = Major.objects.get(id=major_id)

            # Verifica si ya existe un estudiante con la misma cédula
            if Student.objects.filter(cedula=cedula).exists():
                messages.error(request, 'Ya existe un estudiante con esta cédula.')
            # Verifica si ya existe un estudiante con el mismo código
            elif Student.objects.filter(code=code).exists():
                messages.error(request, 'Ya existe un estudiante con este código.')
            else:
                # Crea una instancia de Estudiante y guárdala
                student = Student(
                    name=name,
                    phoneNumber=phoneNumber,
                    date=date,
                    icfes=icfes,
                    cedula=cedula,
                    code=code,
                    mail=mail,
                    major=major_instance
                )
                student.save()

                return redirect(reverse('asignar_scholarship', args=[code]))

        return render(request, 'studentsRegister.html', {'majors':majors, 'form': form, 'mensaje': 'Por favor, complete todos los campos.'})