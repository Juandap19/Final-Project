from django.views import View
from django.shortcuts import render
from follow_students.forms.signin_form import SigninForm
from follow_students.forms.financial_form import FinancialForm
from follow_students.models import User, RolPermiso, Student, Scholarship, Donor, Notification
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

            if user.rol.nombre_rol == "Filantropía":
                students = Student.objects.all()
                scholarship = Scholarship.objects.all()
                donor = Donor.objects.all()
                noti = Notification.objects.all()
                becas_seleccionadas = Scholarship.objects.all()

                return render(request, 'dashboard.html', {
                    'user': user,
                    'num_students': students.count(),
                    'num_scholarship': scholarship.count(),
                    'num_donor': donor.count(),
                    'num_noti': noti.count(),
                    'students': students,
                    'scholarships': scholarship,
                    'donors': donor,
                    'notifications': noti,
                    'becas': becas_seleccionadas,
                })
            
            if user.rol.nombre_rol == "Apoyo Financiero":
                return render(request, 'financial_alimentation.html', {
                    'user': user,
                    'form': FinancialForm(),
                    'error': False
                })

            if user.rol.nombre_rol == "Director de Programa":
                return render(request, 'menuCancelation.html', {
                    'user': user,
                })
            
           
        except ObjectDoesNotExist:
            return render(request, 'index.html', {
                'form': SigninForm(),
                'error': True
            })