from django import forms

class UploadFileForm(forms.Form):
   file = forms.FileField(
      label="Subir Archivo",
      widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
   )