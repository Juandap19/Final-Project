import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from follow_students.forms.upload_dataPD_form import UploadFileForm  
from follow_students.models import Grade,Student,Course
from django.contrib import messages
from django.views import View

# Create your views here.
    
class Upload_dataPD(View):
    def get(self, request):
        form = UploadFileForm()
        grades = Grade.objects.all().order_by('student') 
        return render(request, 'upload_dataPD.html', {
            'form': form,
            'grades': grades})
    
    def post(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if 'file' in request.FILES:
                xls = pd.ExcelFile(request.FILES['file'], engine='openpyxl')
                loaded_data = False  # Variable para rastrear si se cargó algún dato

                for sheet_name in xls.sheet_names:
                    df = pd.read_excel(xls, sheet_name)
                    course, created = Course.objects.get_or_create(code=sheet_name)
                    for index, row in df.iterrows():
                        try:
                            student = Student.objects.get(code=row['Codigo'])
                            grade, created = Grade.objects.get_or_create(
                                student=student,
                                course=course,
                                defaults={'grade': row['NotaCurso']}
                            )
                            if not created:
                                grade.grade = row['NotaCurso']
                                grade.save()
                            loaded_data = True  # Se ha cargado al menos un registro
                        except Student.DoesNotExist:
                            continue
                        except Exception as e:                        
                            messages.error(request, f'Hubo un error al cargar el archivo')
                            return HttpResponseRedirect(request.path)                      

                if not loaded_data:
                    messages.error(request, 'No se cargó ningún dato en la base de datos')
                    return HttpResponseRedirect(request.path)
                
                messages.success(request, 'Se cargó correctamente')
                return HttpResponseRedirect(request.path)

        else:
            form = UploadFileForm()
            grades = Grade.objects.all().order_by('student') 
            return render(request, 'upload_dataPD.html', {
                'form': form,
                'grades': grades})
