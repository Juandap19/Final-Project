from django import forms
from follow_students.models import Beca


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    celular = forms.CharField(max_length=20, required=False)
    fecha = forms.DateField(required=False)
    icfes = forms.IntegerField(required=False)
    cedula = forms.CharField(max_length=20, required=False)
    codigo = forms.CharField(max_length=20, required=False)
    correo = forms.EmailField(required=False)
    major = forms.CharField(max_length=255, required=False)
    beca = forms.ModelChoiceField(queryset=Beca.objects.all(), required=False)