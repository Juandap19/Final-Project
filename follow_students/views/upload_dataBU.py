from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.models import Student, RegisNonAcademicActivity
from follow_students.forms.upload_dataBU import  RegistroActividad
from django.contrib import messages


class Upload_dataBU(View):
    
    def get(self, request):
        form = RegistroActividad()
        activities = RegisNonAcademicActivity.objects.all()
        return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
    
    def post(self, request):
        form = RegistroActividad(request.POST)
        if form.is_valid():
            codigo_student = form.cleaned_data.get('codigo_student')
            try:
                student = Student.objects.get(code=codigo_student)
                actividad = form.cleaned_data.get('actividad')
                dias_asistencia = form.cleaned_data.get('dias_asistencia')
                registro, created = RegisNonAcademicActivity.objects.update_or_create(
                    student=student, 
                    actividad=actividad, 
                    defaults={'dias_asistencia': dias_asistencia},
                )
                if created:
                    messages.success(request, 'Registro de actividad creado exitosamente.')
                    return HttpResponseRedirect(request.path)
                else:
                    messages.success(request, 'Registro de actividad actualizado exitosamente.')
                    return HttpResponseRedirect(request.path)
            except Student.DoesNotExist:
                messages.error(request, 'Este estudiante no existe.')
                form = RegistroActividad()
                activities = RegisNonAcademicActivity.objects.all()
                return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
        else:
            form = RegistroActividad()
            activities = RegisNonAcademicActivity.objects.all()
            return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})


    