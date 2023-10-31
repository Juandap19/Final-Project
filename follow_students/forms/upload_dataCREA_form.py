from django import forms
from follow_students.models import SupportCenter

class RegistroConsulta(forms.Form):
    codigo_student = forms.CharField(max_length=10)
    support_center = forms.ModelChoiceField(queryset=SupportCenter.objects.all())
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    motivo = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
    resultado = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
