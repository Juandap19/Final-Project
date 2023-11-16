from django import forms
from follow_students.models import NonAcademicActivity

class RegisActivity(forms.Form):
    student_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código de estudiante'}),
        label='Código de estudiante'
    )
    activity = forms.ModelChoiceField(
        queryset=NonAcademicActivity.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Actividad'
    )
    assistance_days = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Días de asistencia'}),
        label='Días de asistencia'
    )


