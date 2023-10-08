from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm, FinancialTranspAcademicForm
from follow_students.models import Gasto_beca, Estudiante, Beca , Major,User
from django.contrib import messages
from django.http import HttpResponseRedirect

class FinancialSupport(View):
    def get(self, request):
        return render(request, './financial/financial_alimentation.html', {
            'form': FinancialForm(),
            'error': False
        })
    
    def post(self, request):
        student_code = request.POST['student_code']
        money_quantity = request.POST['money_quantity']
        acumulate_time = request.POST['acumulate_time']
        select_time = request.POST['select_time']
        query = Estudiante.objects.filter(codigo = student_code) # search the student
        if query:
            query = Estudiante.objects.get(codigo = student_code)
            query1 = Beca.objects.get(code = query.beca_id)  #Search the scholarship that is associated with the student 
            new_value = float(query1.montos.alimentacion) - float(money_quantity)  #Calculate the new value
            if new_value > 0:
                query1.montos.alimentacion = new_value
                query1.montos.save() 
                expense =  Gasto_beca.objects.create( estudiante = query, cantidad_dinero = money_quantity, tiempo_acumulado=  acumulate_time, tiempo_seleccionado = select_time, tipo = 'Alimentación')  #Create a expense to One particular Student and save it
                expense.save()   #Save the new value in the data base
                messages.success(request,"Proceso completado")
                return HttpResponseRedirect(request.path)   
            else:
                #Case when the Scholarship doesn`t have enought money to pay the new student money quantity`
                money_quantity = query1.montos.alimentacion
                query1.montos.save()
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
        query = Beca.objects.filter(code = scholarship_code)
        if query:
            scholarship = Beca.objects.get(code = scholarship_code)
            # Calculate the Major that scholarship gonna pay it
            students_list = Estudiante.objects.filter(beca = scholarship_code).values()
            flag = True
            its_missing = 0
            counter_students = 0
            for student in students_list:
                major_aux = Major.objects.get(id = student['major_id'] )
                student_pivot = Estudiante.objects.get(codigo = student['codigo'])
                major_to_add = major_aux.precio
                result_education_fun = scholarship.montos.academico - major_to_add
                if result_education_fun > 0:
                    if student_pivot.aux_academic == 0:
                        student_pivot.aux_academic = 1
                        student_pivot.save()
                        scholarship.montos.academico  = result_education_fun 
                        scholarship.montos.save()
                        expense = Gasto_beca.objects.create( estudiante = student_pivot, beca = scholarship, cantidad_dinero = major_to_add, tiempo_acumulado=  6, tiempo_seleccionado = "Meses", tipo = 'Académico')  #Create a expense to One particular Student and save it
                        expense.save()  
                    else:
                        counter_students += 1      
                else:
                    scholarship.montos.save()
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
        query = Beca.objects.filter(code = scholarship_code)
        if query:
            scholarship = Beca.objects.get(code = scholarship_code)
            # Calculate the Transportation that scholarship gonna pay it
            students_list = Estudiante.objects.filter(beca = scholarship_code).values()
            flag = True
            its_missing = 0
            counter_students = 0
            for student in students_list:
                student_pivot = Estudiante.objects.get(codigo = student['codigo'])
                transportation_fun_result = scholarship.montos.transporte - 1000000
                if transportation_fun_result > 0:
                    if student_pivot.aux_transportation == 0:
                        student_pivot.aux_transportation  = 1
                        student_pivot.save()
                        scholarship.montos.transporte = transportation_fun_result 
                        scholarship.montos.save()
                        expense = Gasto_beca.objects.create( estudiante = student_pivot, beca = scholarship, cantidad_dinero = "1000000", tiempo_acumulado=  6, tiempo_seleccionado = "Meses", tipo = 'Transporte')  #Create a expense to One particular Student and save it
                        expense.save()
                    else:
                        counter_students += 1  
                else:
                    scholarship.montos.save()
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


            
