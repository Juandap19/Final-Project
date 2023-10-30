import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from follow_students.forms.upload_dataPD_form import UploadFileForm  
from follow_students.models import Nota,Student,Curso
from django.contrib import messages
from django.views import View

# Create your views here.
    
class Upload_dataPD(View):
    def get(self, request):
        form = UploadFileForm()
        notas = Nota.objects.all().order_by('student') 
        return render(request, 'upload_dataPD.html', {
            'form': form,
            'notas': notas})
    
    def post(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if 'file' in request.FILES:
                xls = pd.ExcelFile(request.FILES['file'])
                for sheet_name in xls.sheet_names:
                    df = pd.read_excel(xls, sheet_name)
                    curso, created = Curso.objects.get_or_create(code=sheet_name)
                    for index, row in df.iterrows():
                        try:
                            student = Student.objects.get(code=row['Codigo'])
                            nota, created = Nota.objects.get_or_create(
                                student=student,
                                curso=curso,
                                defaults={'grade': row['NotaCurso']}
                            )
                            if not created:
                                nota.grade = row['NotaCurso']
                                nota.save()
                        except Student.DoesNotExist:
                            continue
                        except Exception as e:                        
                            messages.error(request, f'Hubo un error al cargar el archivo')
                            return HttpResponseRedirect(request.path)                      
                messages.success(request, 'Se cargo correctamente')
                return HttpResponseRedirect(request.path)
        else:
            form = UploadFileForm()
            notas = Nota.objects.all().order_by('student') 
            return render(request, 'upload_dataPD.html', {
                'form': form,
                'notas': notas})
    








