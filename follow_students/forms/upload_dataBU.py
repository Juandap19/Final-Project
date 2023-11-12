from django import forms
from follow_students.models import NonAcademicActivity

class RegistroActividad(forms.Form):
    student_code = forms.CharField(max_length=10)
    activity = forms.ModelChoiceField(queryset=NonAcademicActivity.objects.all())
    assitance_days = forms.CharField(max_length=100)


