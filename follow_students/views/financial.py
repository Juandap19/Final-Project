from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm
from follow_students.models import User
from django.core.exceptions import ObjectDoesNotExist

class FinancialSupport(View):
    def get(self, request):
        return render(request, 'financial.html', {
            'form': FinancialForm(),
            'error': False
        })
    def post(self, request):
        student_code = request.POST['student_code']
        quantity = request.POST['quantity']
        days = request.POST['days']
        # it`s missing the post method`