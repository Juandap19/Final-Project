from django import forms

class RegistroConsulta(forms.Form):
    codigo_estudiante = forms.CharField(max_length=10)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    motivo = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
    resultado = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
