from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from follow_students.forms.email_form import SolicitarAct
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

class RequestUpd(View):
    
    def get(self, request):
        form = SolicitarAct()
        return render(request, 'request_update.html', {'form': form})
    
    def post(self, request):
        form = SolicitarAct(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['destinatario']
            subject = form.cleaned_data['asunto']
            message = form.cleaned_data['mensaje']
            from_email = "sistemafilantropia@gmail.com" 
            
            email = EmailMessage(subject, message, from_email, [recipient]) 

            if 'archivo' in request.FILES:
                file = request.FILES['archivo']
                email.attach(file.name, file.read(), file.content_type)

            email.send()
            
            messages.success(request, 'Se ha enviado correctamente')
            return HttpResponseRedirect(request.path)

        else:
            messages.error(request, 'No se ha podido enviar')
            form = SolicitarAct()
            return render(request, 'request_update.html', {'form': form})