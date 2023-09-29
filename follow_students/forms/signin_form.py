from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(
        label = "Usuario",
        max_length = 200,
        widget = forms.TextInput(attrs = {'class': 'input_login d-block container mt-1 mb-3 p-2', 'placeholder': 'Escribe tu usuario', 'autocomplete': 'off'}),
        required = True
    )
    password = forms.CharField(
        label = "Contraseña",
        max_length = 200,
        widget = forms.PasswordInput(attrs = {'class': 'input_login d-block container mt-1 mb-3 p-2', 'placeholder': 'Escribe tu contraseña'}),
        required = True
    )