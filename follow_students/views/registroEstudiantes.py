from django.views import View
from django.shortcuts import render, redirect
from follow_students.forms.registroEstudiantes_form import EstudianteForm
from follow_students.models import Estudiante  

class RegistroEstudiantes(View):
    def get(self, request):
        title = "Django Course!!"
        form = EstudianteForm()
        return render(request, 'registroEstudiantes.html', {'title': title, 'form': form, 'mensaje': None})

    def post(self, request):
        form = EstudianteForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            celular = form.cleaned_data['celular']
            fecha = form.cleaned_data['fecha']
            icfes = form.cleaned_data['icfes']
            cedula = form.cleaned_data['cedula']
            codigo = form.cleaned_data['codigo']
            correo = form.cleaned_data['correo']

            estudiante = Estudiante(
                nombre=nombre,
                celular=celular,
                fecha=fecha,
                icfes=icfes,
                cedula=cedula,
                codigo=codigo,
                correo=correo
            )
            estudiante.save()

            return render(request, 'registroExitoso.html', {'nombre': nombre})

        return render(request, 'registroEstudiantes.html', {'form': form, 'mensaje': 'Por favor, complete todos los campos.'})
