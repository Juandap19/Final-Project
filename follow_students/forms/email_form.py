from django import forms

class SolicitarAct(forms.Form):
    destinatario = forms.EmailField(label='Destinatario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    asunto = forms.CharField(label='Asunto', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Mensaje')
    archivo = forms.FileField(label='Adjuntar archivo (Opcional)', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
