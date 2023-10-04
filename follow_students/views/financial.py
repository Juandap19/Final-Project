from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm
from follow_students.models import Scholarship_Expenses, Student
from django.contrib import messages
from django.http import HttpResponseRedirect


class FinancialSupport(View):
    def get(self, request):
        return render(request, 'financial.html', {
            'form': FinancialForm(),
            'error': False
        })
    def post(self, request):
        student_code = request.POST['student_code']
        money_quantity = request.POST['money_quantity']
        acumulate_time = request.POST['acumulate_time']
        select_time = request.POST['select_time']
       # Search the student
        query = Student.objects.filter(code = student_code)
        if query:
            #Create a expense to One particular Student
            expense = Scholarship_Expenses.objects.create(student_code = student_code, money_quantity = money_quantity, acumulate_time=  acumulate_time, select_time = select_time)
            expense.save()
            messages.success(request,"Proceso completado")
            return HttpResponseRedirect(request.path)
        else:
            messages.error(request,"El codigo "+ student_code + " no existe")
            return HttpResponseRedirect(request.path)
            
        