from django.views import View
from django.shortcuts import render
from follow_students.forms.signin_form import SigninForm
from follow_students.models import User, RolPermiso
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

class Signin(View):
    def get(self, request):
        return render(request, 'index.html', {
            'form': SigninForm(),
            'error': False
        })
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username, password = password)
            permisos = [p.permiso.nombre_permiso for p in RolPermiso.objects.filter(rol=user.rol)]
            request.session['permisos'] = permisos
            request.session['rol'] = user.rol.nombre_rol
            request.session['name'] = user.name

            return render(request, 'dashboard.html', {
                'user': user
            })
        except ObjectDoesNotExist:
            return render(request, 'index.html', {
                'form': SigninForm(),
                'error': True
            })