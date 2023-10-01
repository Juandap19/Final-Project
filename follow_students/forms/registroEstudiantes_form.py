from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    celular = forms.CharField(max_length=20, required=True)
    fecha = forms.DateField(required=True)
    icfes = forms.IntegerField(required=True)
    cedula = forms.CharField(max_length=20, required=True)
    codigo = forms.CharField(max_length=20, required=True)
    correo = forms.EmailField(required=True)