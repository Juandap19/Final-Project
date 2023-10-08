from django import forms

class RegistroConsulta(forms.Form):
    codigo_estudiante = forms.CharField(max_length=10)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    motivo = forms.CharField(widget=forms.Textarea, max_length=200)
    resultado = forms.CharField(widget=forms.Textarea, max_length=200)
