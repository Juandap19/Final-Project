from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.models import Student, Consulta
from follow_students.forms.upload_dataCREA_form import RegistroConsulta
from django.contrib import messages


class Upload_dataCREA(View):
    
    def get(self, request):
        form = RegistroConsulta()
        consultas = Consulta.objects.all()
        return render(request, 'upload_dataCREA.html', {'form': form, 'consultas': consultas})
    
    def post(self, request):
        form = RegistroConsulta(request.POST)
        if form.is_valid():
            codigo_student = form.cleaned_data.get('codigo_student')
            try:
                student = Student.objects.get(code=codigo_student)
            except Student.DoesNotExist:
                messages.error(request, 'Este estudiante no existe.')
                form = RegistroConsulta()
                consultas = Consulta.objects.all()
                return render(request, 'upload_dataCREA.html', {'form': form, 'consultas': consultas})

            fecha = form.cleaned_data.get('fecha')
            hora = form.cleaned_data.get('hora')
            motivo = form.cleaned_data.get('motivo')
            resultado = form.cleaned_data.get('resultado')
            Consulta.objects.create(
                student=student, 
                fecha=fecha,
                hora=hora,
                motivo=motivo,
                resultado=resultado
            )
            messages.success(request, 'Consulta registrada exitosamente.')
            return HttpResponseRedirect(request.path)
        else:
            form = RegistroConsulta()
            consultas = Consulta.objects.all()
            return render(request, 'upload_dataCREA.html', {'form': form, 'consultas': consultas})
