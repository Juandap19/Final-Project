from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.models import Estudiante, RegistroActividadEstudiante
from follow_students.forms.upload_dataBU import  RegistroActividad
from django.contrib import messages


class Upload_dataBU(View):
    
    def get(self, request):
        form = RegistroActividad()
        activities = RegistroActividadEstudiante.objects.all()
        return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
    
    def post(self, request):
        form = RegistroActividad(request.POST)
        if form.is_valid():
            codigo_estudiante = form.cleaned_data.get('codigo_estudiante')
            try:
                estudiante = Estudiante.objects.get(codigo=codigo_estudiante)
                actividad = form.cleaned_data.get('actividad')
                dias_asistencia = form.cleaned_data.get('dias_asistencia')
                registro, created = RegistroActividadEstudiante.objects.update_or_create(
                    estudiante=estudiante, 
                    actividad=actividad, 
                    defaults={'dias_asistencia': dias_asistencia},
                )
                if created:
                    messages.success(request, 'Registro de actividad creado exitosamente.')
                    return HttpResponseRedirect(request.path)
                else:
                    messages.success(request, 'Registro de actividad actualizado exitosamente.')
                    return HttpResponseRedirect(request.path)
            except Estudiante.DoesNotExist:
                messages.error(request, 'Este estudiante no existe.')
                form = RegistroActividad()
                activities = RegistroActividadEstudiante.objects.all()
                return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
        else:
            form = RegistroActividad()
            activities = RegistroActividadEstudiante.objects.all()
            return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})


    