from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError




def log_in(request): 
     if request.method == 'GET' :
          return render(request, 'log_in.html', {
               'form': AuthenticationForm
          })
     else:
          user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
          if user is None:
               return HttpResponse('No existe el usuario')
          else:
            login(request, user)
            return redirect( "/post_log")
          

def post_log(request):
    return render(request,'post_log.html')


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html',{
            'form': UserCreationForm , 
            'title': 'Sign In'
        })
    else:
        if request.POST['password1'] ==  request.POST['password2']:
          try:
               user = User.objects.create_user(username =  request.POST['username'], password = request.POST['password1'])
               user.save()
               return redirect('/post_log')
          except IntegrityError :
               return HttpResponse('Usuario ya existe')   
           
          return HttpResponse('Contrasenas incorrectas')
        
def signout(request):
    logout(request)
    return redirect('log_in')
         


