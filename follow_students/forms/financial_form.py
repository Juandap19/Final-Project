from django import forms

class FinancialForm(forms.Form):
    student_code = forms.CharField(
        label = "Código estudiante",
        max_length= 200,
        widget =  forms.TextInput(  attrs = {'class': 'input_code d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite el codigo'}),
        required = True
    )
   
    quantity = forms.FloatField(
        label = "Valor Acumulado",
        widget =  forms.TextInput(  attrs = {'class': 'input_quantity d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite el valor'}),
        required = True
    )
   
    days = forms.IntegerField(
        label = "Dias acumulados",
        widget =  forms.TextInput(  attrs = {'class': 'input_days d-block container mt-1 mb-3 p-2', 'placeholder': 'Digite los días'}),
        required = True
    )