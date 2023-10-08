from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm, FinancialTranspAcademicForm
from follow_students.models import Scholarship_Expense, Student, Scholarship , Major,User
from django.contrib import messages
from django.http import HttpResponseRedirect
import random


class FinancialSupport(View):
    def get(self, request):
        return render(request, './financial/financial_alimentation.html', {
            'form': FinancialForm(),
            'error': False
        })
    
    def post(self, request):
        usuario_prueba = User.objects.get()
        code = random.randint(0,50000000000)
        student_code = request.POST['student_code']
        money_quantity = request.POST['money_quantity']
        acumulate_time = request.POST['acumulate_time']
        select_time = request.POST['select_time']
        query = Student.objects.filter(code = student_code) # search the student
        if query:
            query = Student.objects.get(code = student_code)
            query1 = Scholarship.objects.get(code = query.scholarship_id.code)  #Search the scholarship that is associated with the student 
            new_value = float(query1.code_Funds.alimentation_fund) - float(money_quantity)  #Calculate the new value
            if new_value > 0:
                query1.code_Funds.alimentation_fund = new_value
                query1.code_Funds.save() 
                expense = Scholarship_Expense.objects.create( student_code = student_code, money_quantity = money_quantity, acumulate_time=  acumulate_time, select_time = select_time,type = 'Alimentación')  #Create a expense to One particular Student and save it
                expense.save()   #Save the new value in the data base
                messages.success(request,"Proceso completado")
                return HttpResponseRedirect(request.path)   
            else:
                #Case when the Scholarship doesn`t have enought money to pay the new student money quantity`
                money_quantity = query1.code_Funds.alimentation_fund
                query1.code_Funds.save()  
                expense = Scholarship_Expense.objects.create(student_code = student_code, money_quantity = money_quantity, acumulate_time=  acumulate_time, select_time = select_time, type = 'Alimentación')  #Create a expense to One particular Student and save it
                expense.save()
                new_value = abs(new_value)
                messages.warning(request,"Fondos insuficientes de alimentación faltan {} para registrar el pago".format(new_value))
                return  HttpResponseRedirect(request.path)   
        else:
            messages.error(request,"El codigo del estudiante {}  no existe ".format( student_code ))
            return HttpResponseRedirect(request.path)
        
    
class FinancialAcademic(View):
    def get(self, request):
         return render(request, './financial/financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Académico"
        })
    
    def post(self, request):
        scholarship_code = request.POST['scholarship_code']
        query = Scholarship.objects.filter(code = scholarship_code)
        if query:
            scholarship = Scholarship.objects.get(code = scholarship_code)
            # Calculate the Major that scholarship gonna pay it
            students_list = Student.objects.filter(scholarship_id = scholarship_code).values()
            flag = True
            its_missing = 0
            counter_students = 0
            for student in students_list:
                major_aux = Major.objects.get(major_code = student['major_code_id'] )
                student_pivot = Student.objects.get(code = student['code'])
                major_to_add = major_aux.value
                result_education_fun = scholarship.code_Funds.education_fund - major_to_add
                if result_education_fun > 0:
                    if student_pivot.aux_academic == 0:
                        student_pivot.aux_academic = 1
                        student_pivot.save()
                        scholarship.code_Funds.education_fund = result_education_fun 
                        scholarship.code_Funds.save()
                        expense = Scholarship_Expense.objects.create( student_code = student['code'], money_quantity = major_to_add, acumulate_time=  6, select_time = "Meses", type = 'Académico')  #Create a expense to One particular Student and save it
                        expense.save()  
                    else:
                        counter_students += 1      
                else:
                    scholarship.code_Funds.save()
                    flag = False
                    its_missing += 1 

            if flag:
                if counter_students != len(students_list):
                    messages.success(request,"Proceso completado")
                    return HttpResponseRedirect(request.path)
                else:
                    messages.info(request,"Los estudiantes de la beca {} ya han sido pagado".format(scholarship_code))
                    return HttpResponseRedirect(request.path)
            else:
                messages.Warning(request,"Fondos insuficientes faltan: {} estudiantes por matricular".format(its_missing))
                return HttpResponseRedirect(request.path)
        else:
            messages.error(request,"El codigo de la beca {} no existe".format(scholarship_code))
            return HttpResponseRedirect(request.path)

class FinancialTransport(View):
    def get(self, request):
         return render(request, './financial/financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Transporte"
        })
    
    def post(self, request):
        scholarship_code = request.POST['scholarship_code']
        query = Scholarship.objects.filter(code = scholarship_code)
        if query:
            scholarship = Scholarship.objects.get(code = scholarship_code)
            # Calculate the Transportation that scholarship gonna pay it
            students_list = Student.objects.filter(scholarship_id = scholarship_code).values()
            flag = True
            its_missing = 0
            counter_students = 0
            for student in students_list:
                student_pivot = Student.objects.get(code = student['code'])
                transportation_fun_result = scholarship.code_Funds.transportation_fund - 1000000
                if transportation_fun_result > 0:
                    if student_pivot.aux_transportation == 0:
                        student_pivot.aux_transportation  = 1
                        student_pivot.save()
                        scholarship.code_Funds.transportation_fund = transportation_fun_result 
                        scholarship.code_Funds.save()
                        expense = Scholarship_Expense.objects.create( student_code = student['code'], money_quantity = "1000000", acumulate_time=  6, select_time = "Meses", type = 'Transporte')  #Create a expense to One particular Student and save it
                        expense.save()
                    else:
                        counter_students += 1  
                else:
                    scholarship.code_Funds.save()
                    flag = False
                    its_missing += 1 

            if flag:
                if counter_students != len(students_list):
                    messages.success(request,"Proceso completado")
                    return HttpResponseRedirect(request.path)
                else:
                    messages.info(request,"Los auxilios de transporte de la beca {} ya han sido pagado".format(scholarship_code))
                    return HttpResponseRedirect(request.path) 
            else:
                messages.warning(request,"Fondos insuficientes faltan: {} estudiantes por auxilio de transporte".format(its_missing))
                return HttpResponseRedirect(request.path)
        else:
            messages.error(request,"El codigo de la beca {} no existe".format(scholarship_code))
            return HttpResponseRedirect(request.path)


            
        