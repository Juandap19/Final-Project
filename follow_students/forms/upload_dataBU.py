from django import forms
from follow_students.models import NonAcademicActivity

class RegisActivity(forms.Form):
    student_code = forms.CharField(max_length=10)
    activity = forms.ModelChoiceField(queryset=NonAcademicActivity.objects.all())
    assistance_days = forms.CharField(max_length=100)


