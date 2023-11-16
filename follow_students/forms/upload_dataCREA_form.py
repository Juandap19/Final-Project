from django import forms
from follow_students.models import SupportCenter

class RegisConsult(forms.Form):
    student_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label = "Codigo estudiante"
    )
    support_center = forms.ModelChoiceField(
        queryset=SupportCenter.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label = "Centro de soporte"
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label = "Fecha"
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        label = "Hora"
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;', 'class': 'form-control'}),
        label = "Razon"
    )
    outcome = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;', 'class': 'form-control'}),
        label = "Resultado"
    )
