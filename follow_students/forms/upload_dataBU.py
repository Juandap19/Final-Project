from django import forms
from follow_students.models import ActividadNoAcademica

class RegistroActividad(forms.Form):
    codigo_student = forms.CharField(max_length=10)
    actividad = forms.ModelChoiceField(queryset=ActividadNoAcademica.objects.all())
    dias_asistencia = forms.CharField(max_length=100)


