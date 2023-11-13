from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.models import Student, RegisNonAcademicActivity
from follow_students.forms.upload_dataBU import  RegisActivity
from django.contrib import messages


class Upload_dataBU(View):
    
    def get(self, request):
        form = RegisActivity()
        activities = RegisNonAcademicActivity.objects.all()
        return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
    
    def post(self, request):
        form = RegisActivity(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data.get('student_code')
            try:
                student = Student.objects.get(code=student_code)
                activity = form.cleaned_data.get('activity')
                assistance_days = form.cleaned_data.get('assistance_days')
                regis, created = RegisNonAcademicActivity.objects.update_or_create(
                    student=student, 
                    activity=activity, 
                    defaults={'assistance_days': assistance_days},
                )
                if created:
                    messages.success(request, 'Registro de actividad creado exitosamente.')
                    return HttpResponseRedirect(request.path)
                else:
                    messages.success(request, 'Registro de actividad actualizado exitosamente.')
                    return HttpResponseRedirect(request.path)
            except Student.DoesNotExist:
                messages.error(request, 'Este estudiante no existe.')
                form = RegisActivity()
                activities = RegisNonAcademicActivity.objects.all()
                return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})
        else:
            form = RegisActivity()
            activities = RegisNonAcademicActivity.objects.all()
            return render(request, 'upload_dataBU.html', {'form': form, 'activities': activities})


    