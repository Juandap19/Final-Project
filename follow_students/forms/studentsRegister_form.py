from django import forms
from follow_students.models import Scholarship


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    phoneNumber = forms.CharField(max_length=20, required=False)
    date = forms.DateField(required=False)
    icfes = forms.IntegerField(required=False)
    cedula = forms.CharField(max_length=20, required=False)
    code = forms.CharField(max_length=20, required=False)
    mail = forms.EmailField(required=False)
    major = forms.CharField(max_length=255, required=False)
    scholarship = forms.ModelChoiceField(queryset=Scholarship.objects.all(), required=False)