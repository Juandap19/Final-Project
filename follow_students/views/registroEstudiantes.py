from django.views import View
from django.shortcuts import render, redirect
from follow_students.forms.registroEstudiantes_form import EstudianteForm
from follow_students.models import Estudiante, Major  
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.utils import IntegrityError 


class RegistroEstudiantes(View):
    def get(self, request):
        title = "Django Course!!"
        majors = Major.objects.all()
        form = EstudianteForm()
        return render(request, 'registroEstudiantes.html', {'title': title,'majors':majors, 'form': form, 'mensaje': None})

    def post(self, request):
        majors = Major.objects.all()
        form = EstudianteForm(request.POST)

        if form.is_valid():
            # Extrae los datos del formulario
            nombre = form.cleaned_data['nombre']
            celular = form.cleaned_data['celular']
            fecha = form.cleaned_data['fecha']
            icfes = form.cleaned_data['icfes']
            cedula = form.cleaned_data['cedula']
            codigo = form.cleaned_data['codigo']
            correo = form.cleaned_data['correo']
            major_id = form.cleaned_data['major']
            major_instance = Major.objects.get(id=major_id)

            # Verifica si ya existe un estudiante con la misma cédula
            if Estudiante.objects.filter(cedula=cedula).exists():
                messages.error(request, 'Ya existe un estudiante con esta cédula.')
            # Verifica si ya existe un estudiante con el mismo código
            elif Estudiante.objects.filter(codigo=codigo).exists():
                messages.error(request, 'Ya existe un estudiante con este código.')
            else:
                # Crea una instancia de Estudiante y guárdala
                estudiante = Estudiante(
                    nombre=nombre,
                    celular=celular,
                    fecha=fecha,
                    icfes=icfes,
                    cedula=cedula,
                    codigo=codigo,
                    correo=correo,
                    major=major_instance
                )
                estudiante.save()

                return redirect(reverse('asignar_beca', args=[codigo]))

        return render(request, 'registroEstudiantes.html', {'majors':majors, 'form': form, 'mensaje': 'Por favor, complete todos los campos.'})