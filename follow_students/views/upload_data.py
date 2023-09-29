import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from follow_students.forms.upload_data_form import UploadFileForm  
from follow_students.models import DataDP
from django.contrib import messages
from django.views import View

# Create your views here.
    
class Load_data(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'upload_data.html',  {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if 'file' in request.FILES:
                df = pd.read_excel(request.FILES['file'])
                for index, row in df.iterrows():
                    try:
                        obj, created = DataDP.objects.update_or_create(
                            code=row['Codigo'],
                            defaults={'grade1': row['Nota 1'], 'grade2': row['Nota 2'], 'grade3': row['Nota 3']}
                        )
                    except Exception as e:
                        messages.error(request, f'Hubo un error al crear o actualizar el objeto: {str(e)}')
                        return HttpResponseRedirect(request.path)
            messages.success(request, 'Se cargo correctamente')
            return HttpResponseRedirect(request.path)
        else:
            form = UploadFileForm()
            return render(request, 'load_page.html', {'form': form})