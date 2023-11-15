from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student
from follow_students.forms.signin_form import SigninForm

class Logout(View):
    def get(self, request):
        return redirect('signin')
