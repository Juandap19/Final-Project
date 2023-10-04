from django import forms

time_options = [
    ('Days', 'Dias'),
    ('Month', 'Mes'),
    ('Year', 'Año'),
]

class FinancialForm(forms.Form):
    student_code = forms.CharField(
        label = "Código estudiante ",
        max_length= 200,
        widget =  forms.TextInput(  attrs = {'class': 'input_code d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite el codigo  '}),
        required = True
    )
   
    money_quantity = forms.FloatField(
        label = "Valor Acumulado",
        widget =  forms.TextInput(  attrs = {'class': 'input_quantity d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite el valor'}),
        required = True
    )

    acumulate_time = forms.IntegerField(
        label = "Tiempo Acumulado",
        widget =  forms.TextInput(  attrs = {'class': 'input_quantity d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite el valor'}),
        required = True

    )   

    select_time = forms.ChoiceField(
        choices = time_options, 
        required=True, 
        label= "Seleccione una opción"
    )


