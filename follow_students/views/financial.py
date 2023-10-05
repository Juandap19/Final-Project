from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm
from follow_students.models import Scholarship_Expenses, Student, Scholarship, Scholarship_Funds
from django.contrib import messages
from django.http import HttpResponseRedirect
import random


class FinancialSupport(View):
    def get(self, request):
        return render(request, 'financial.html', {
            'form': FinancialForm(),
            'error': False
        })
    def post(self, request):
        code =random.randint(0,50000000000)
        student_code = request.POST['student_code']
        money_quantity = request.POST['money_quantity']
        acumulate_time = request.POST['acumulate_time']
        select_time = request.POST['select_time']
        query = Student.objects.filter(code = student_code) # search the student
        if query:
            query = Student.objects.get(code = student_code)
            query1 = Scholarship.objects.get(code = query.scholarship_id.code)  #Search the scholarship that is associated with the student 
            new_value = float(query1.code_Funds.alimentation_fund) - float(money_quantity)  #Calculate the new value
            if(new_value > 0):
                query1.code_Funds.alimentation_fund = new_value
                query1.code_Funds.save() 
                expense = Scholarship_Expenses.objects.create(code = code , student_code = student_code, money_quantity = money_quantity, acumulate_time=  acumulate_time, select_time = select_time)  #Create a expense to One particular Student and save it
                expense.save()   #Save the new value in the data base
                messages.success(request,"Proceso completado")
                return HttpResponseRedirect(request.path)   
            else:
                #Case when the Scholarship doesn`t have enought money to pay the new student money quantity`
                money_quantity = query1.code_Funds.alimentation_fund
                query1.code_Funds.alimentation_fund = 0
                query1.code_Funds.save()  
                expense = Scholarship_Expenses.objects.create(code = code , student_code = student_code, money_quantity = money_quantity, acumulate_time=  acumulate_time, select_time = select_time)  #Create a expense to One particular Student and save it
                expense.save()
                new_value = abs(new_value)
                messages.warning(request,"Se acabo el monto de la beca falta por pagar: {}".format(new_value))
                return  HttpResponseRedirect(request.path)   
        else:
            messages.error(request,"El codigo "+ student_code + " no existe")
            return HttpResponseRedirect(request.path)
        
    
        
    

            
        