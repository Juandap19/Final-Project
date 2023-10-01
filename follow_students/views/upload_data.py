import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from follow_students.forms.upload_data_form import UploadFileForm  
from follow_students.models import Nota,Estudiante,Curso
from django.contrib import messages
from django.views import View

# Create your views here.
    
class Load_data(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'upload_data.html', {
            'form': form})
    
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
                            estudiante, created = Estudiante.objects.get_or_create(code=row['Codigo'])
                            nota, created = Nota.objects.get_or_create(
                                estudiante=estudiante,
                                curso=curso,
                                defaults={'grade': row['NotaCurso']}
                            )
                        except Exception as e:                        
                            messages.error(request, f'Hubo un error al cargar el archivo')
                            return HttpResponseRedirect(request.path)                      
                messages.success(request, 'Se cargo correctamente')
                return HttpResponseRedirect(request.path)
        else:
            form = UploadFileForm()
            return render(request, 'upload_page.html', {
                'form': form})




