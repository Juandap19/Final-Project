from django.views import View
from django.shortcuts import render
from follow_students.forms.signin_form import SigninForm
from follow_students.models import User
from django.core.exceptions import ObjectDoesNotExist

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
            return render(request, 'dashboard.html', {
                'user': user
            })
        except ObjectDoesNotExist:
            return render(request, 'index.html', {
                'form': SigninForm(),
                'error': True
            })