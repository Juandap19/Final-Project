from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.models import Student, Consult
from follow_students.forms.upload_dataCREA_form import RegisConsult
from django.contrib import messages


class Upload_dataCREA(View):
    
    def get(self, request):
        form = RegisConsult()
        consultations = Consult.objects.all()
        return render(request, 'upload_dataCREA.html', {'form': form, 'consultations': consultations})
    
    def post(self, request):
        form = RegisConsult(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data.get('student_code')
            try:
                student = Student.objects.get(code=student_code)
            except Student.DoesNotExist:
                messages.error(request, 'Este estudiante no existe.')
                form = RegisConsult()
                consultations = Consult.objects.all()
                return render(request, 'upload_dataCREA.html', {'form': form, 'consultations': consultations})

            support_center = form.cleaned_data.get('support_center')
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            reason = form.cleaned_data.get('reason')
            outcome = form.cleaned_data.get('outcome')
            Consult.objects.create(
                student=student, 
                support_center=support_center,
                date=date,
                time=time,
                reason=reason,
                outcome=outcome
            )
            messages.success(request, 'Consulta registrada exitosamente.')
            return HttpResponseRedirect(request.path)
        else:
            form = RegisConsult()
            consultations = Consult.objects.all()
            return render(request, 'upload_dataCREA.html', {'form': form, 'consultations': consultations})
