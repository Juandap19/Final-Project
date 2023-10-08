from django import forms

class SolicitarAct(forms.Form):
    destinatario = forms.EmailField(label='Destinatario')
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
    archivo = forms.FileField(label='Adjuntar archivo (Opcional)', required=False)
