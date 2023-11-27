from django import forms

time_options = [
    ('Dias', 'Dias'),
    ('Mes', 'Mes'),
    ('Año', 'Año'),
]

class FinancialForm(forms.Form):
    student_code = forms.CharField(
        label = "Código estudiante ",
        max_length= 200,
        widget =  forms.TextInput(  attrs = {'class': 'form-control', 'placeholder': 'Digite el codigo  '}),
        required = True
    )
   
    money_quantity = forms.FloatField(
        label = "Valor Acumulado",
        widget =  forms.TextInput(  attrs = {'class': 'form-control', 'placeholder': 'Digite el valor'}),
        required = True
    )

    acumulate_time = forms.IntegerField(
        label = "Tiempo Acumulado",
        widget =  forms.TextInput(  attrs = {'class': 'form-control', 'placeholder': 'Digite el valor'}),
        required = True

    )   

    select_time = forms.ChoiceField(
        choices=time_options,
        required=True,
        label="Seleccione una opción",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class FinancialTranspAcademicForm(forms.Form):
    scholarship_code = forms.CharField(
        label = "Pago de Beca",
        max_length= 200,
        widget =  forms.TextInput(  attrs = {'class': 'input_code d-block container mt-0 mb-0 p-0', 'placeholder': 'Codigo de Beca' }),
        required = True
    )

class FinancialTAByStudentForm(forms.Form):
    student_code = forms.CharField(
        label = "Pago por estudiante ",
        max_length= 200,
        widget =  forms.TextInput(  attrs = {'class': 'input_code d-block container mt-0 mb-0 p-0', 'placeholder': 'Codigo del estudiante'}),
        required = True
    )
   