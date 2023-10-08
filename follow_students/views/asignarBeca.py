from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from follow_students.forms.registroEstudiantes_form import EstudianteForm
from follow_students.models import Estudiante, Beca
from django.contrib import messages
from django.http import HttpResponseRedirect

class AsignarBeca(View):
    def get(self, request, codigo):
        student = get_object_or_404(Estudiante, codigo=codigo)
        title = "Django Course!!"
        form = EstudianteForm()
        becas = Beca.objects.all()
        return render(request, 'asignarBeca.html', {'title': title, 'form': form, 'mensaje': None, 'becas': becas, 'codigo': codigo, 'student': student})
    
    def post(self, request, codigo):
        becas = Beca.objects.all()
        student = get_object_or_404(Estudiante, codigo=codigo)
        form = EstudianteForm(request.POST)

        if form.is_valid():
            # Obtener el ID de la beca seleccionada (si se proporcionó)
            beca_id = request.POST.get('beca_id')

            # Verificar si se ha seleccionado una beca
            if beca_id:
                nueva_beca = get_object_or_404(Beca, id=beca_id)

                # Disminuir el contador de estudiantes asignados en la beca anterior (si tenía una beca previa)
                if student.beca:
                    student.beca.estudiantes_asignados -= 1
                    student.beca.save()

                # Aumentar el contador de estudiantes asignados en la nueva beca
                nueva_beca.estudiantes_asignados += 1
                nueva_beca.save()

                # Asignar la nueva beca al estudiante
                student.beca = nueva_beca
                student.save()

                messages.success(request, "Beca asignada exitosamente")
                return redirect('asignar_beca', codigo=codigo)
            else:
                messages.error(request, "Por favor, seleccione una beca antes de continuar.")
        else:
            messages.error(request, "El formulario no es válido. Por favor, complete todos los campos.")

        return render(request, 'asignarBeca.html', {'becas': becas, 'form': form, 'codigo': codigo, 'student': student})
