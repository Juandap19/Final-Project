from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm, FinancialTranspAcademicForm , FinancialTAByStudentForm
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
            print("adfadf{}".format(query.beca_id))
            query1 = Beca.objects.get(id = query.beca_id)  #Search the scholarship that is associated with the student 
            new_value = float(query1.montos.alimentacion) - float(money_quantity)  #Calculate the new value
            if new_value >= 0:
                query1.montos.alimentacion = new_value
                query1.montos.save() 
                expense =  Gasto_beca.objects.create( estudiante = query, cantidad_dinero = money_quantity, tiempo_acumulado=  acumulate_time, tiempo_seleccionado = select_time, tipo = 'Alimentación', beca = query1)  #Create a expense to One particular Student and save it
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
         missing_scholarship = []        
         students_list = Estudiante.objects.all()
         for student_pivot in students_list:
             if student_pivot.aux_academic == "0":
                if student_pivot.beca not in missing_scholarship:
                    missing_scholarship.append(student_pivot.beca)
         return render(request, './financial/financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Académico",
            'becas_faltantes': missing_scholarship,
            'student_form': FinancialTAByStudentForm(),
        })
    
    def post(self, request):
        student_form = request.POST.get('student_code')
        if student_form:
            student = Estudiante.objects.filter(codigo = student_form )
            if student:
                student = Estudiante.objects.get(codigo = student_form )
                scholarship = student.beca
                academic_fun_result = round(student.major.precio * (scholarship.porcentaje_academico/100))
                if student.aux_academic == "0":
                    if academic_fun_result >= 0:
                        student.aux_academic  = "1"
                        student.save()
                        scholarship.montos.transporte = academic_fun_result 
                        scholarship.montos.save()
                        expense = Gasto_beca.objects.create( estudiante = student, beca = scholarship, cantidad_dinero = academic_fun_result, tiempo_acumulado =  6, tiempo_seleccionado = "Meses", tipo = 'Academico')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado".format(student.codigo ))
                        return HttpResponseRedirect(request.path) 
                    else:
                        messages.warning(request,"Pago no aprobado Fondos insuficientes de la beca")
                        return HttpResponseRedirect(request.path)
                        
                else:
                    messages.info(request,"El estudiante asociado con el codigo {} ya ha sido pagado previamente".format(student.codigo))
                    return HttpResponseRedirect(request.path) 
            else:
                messages.error(request,"No existe el codigo {} en el sistema de becados".format(student_form))
                return HttpResponseRedirect(request.path)  
        else:
            scholarship_code = request.POST['scholarship_code']
            query = Beca.objects.filter(code = scholarship_code)
            if query:
                scholarship = Beca.objects.get(code = scholarship_code)
                # Calculate the Major that scholarship gonna pay it
                students_list = Estudiante.objects.filter(beca = scholarship).values()
                flag = True
                its_missing = 0
                counter_students = 0
                for student in students_list:
                    major_aux = Major.objects.get(id = student['major_id'] )
                    student_pivot = Estudiante.objects.get(codigo = student['codigo'])
                    major_to_add = round(major_aux.precio * float(scholarship.porcentaje_academico/100))
                    result_education_fun = scholarship.montos.academico - major_to_add
                    if student_pivot.aux_academic == "0":
                        if result_education_fun >= 0:
                            student_pivot.aux_academic = "1"
                            student_pivot.save()
                            scholarship.montos.academico  = result_education_fun 
                            scholarship.montos.save()
                            expense = Gasto_beca.objects.create( estudiante = student_pivot, beca = scholarship, cantidad_dinero = major_to_add, tiempo_acumulado =  6, tiempo_seleccionado = "Meses", tipo = 'Académico')  #Create a expense to One particular Student and save it
                            expense.save()   
                        else:
                            scholarship.montos.save()
                            flag = False
                            its_missing += 1 
                    else:
                        counter_students += 1     
                if flag:
                    if counter_students != len(students_list):
                        messages.success(request,"Proceso completado")
                        return HttpResponseRedirect(request.path)
                    else:
                        messages.info(request,"Los estudiantes de la beca {} ya han sido pagado".format(scholarship_code))
                        return HttpResponseRedirect(request.path)
                else:
                    messages.warning(request,"Fondos insuficientes faltan: {} estudiantes por matricular".format(its_missing))
                    return HttpResponseRedirect(request.path)
            else:
                messages.error(request,"El codigo de la beca {} no existe".format(scholarship_code))
                return HttpResponseRedirect(request.path)

class FinancialTransport(View):
    def get(self, request):
        missing_scholarship = []        
        students_list = Estudiante.objects.all()
        for student_pivot in students_list:
            if student_pivot.aux_transportation == "0":
                if student_pivot.beca not in missing_scholarship:
                    missing_scholarship.append(student_pivot.beca)
        return render(request, './financial/financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Transporte",
            'becas_faltantes': missing_scholarship,
            'student_form': FinancialTAByStudentForm(),
        })
    def post(self, request):
        student_form = request.POST.get('student_code')
        if student_form:
            student = Estudiante.objects.filter(codigo = student_form )
            if student:
                student = Estudiante.objects.get(codigo = student_form )
                scholarship = student.beca
                transportation_fun_result = scholarship.montos.transporte - scholarship.auxilio_transporte
                if student.aux_transportation == "0":
                    if transportation_fun_result >= 0:
                        student.aux_transportation  = "1"
                        student.save()
                        scholarship.montos.transporte = transportation_fun_result 
                        scholarship.montos.save()
                        expense = Gasto_beca.objects.create( estudiante = student, beca = scholarship, cantidad_dinero = scholarship.auxilio_transporte, tiempo_acumulado =  6, tiempo_seleccionado = "Meses", tipo = 'Transporte')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado".format(student))
                        return HttpResponseRedirect(request.path) 
                    else:
                        messages.warning(request,"Pago no aprobado Fondos insuficientes de la beca")
                        return HttpResponseRedirect(request.path)
                else:
                    messages.info(request,"El estudiante asociado con el codigo {} ya ha sido pagado previamente".format(student))
                    return HttpResponseRedirect(request.path) 
            else:
                messages.error(request,"No existe el codigo {} en el sistema de becados".format(student_form))
                return HttpResponseRedirect(request.path)  
        else:
                scholarship_code = request.POST['scholarship_code']
                query = Beca.objects.filter(code = scholarship_code)
                if query:
                    scholarship = Beca.objects.get(code = scholarship_code)
                    # Calculate the Transportation that scholarship gonna pay it
                    students_list = Estudiante.objects.filter(beca = scholarship).values()
                    flag = True
                    its_missing = 0
                    counter_students = 0
                    for student in students_list:
                        student_pivot = Estudiante.objects.get(codigo = student['codigo'])
                        transportation_fun_result = scholarship.montos.transporte - scholarship.auxilio_transporte
                        if student_pivot.aux_transportation == "0": 
                            if  transportation_fun_result >= 0:
                                student_pivot.aux_transportation  = "1"
                                student_pivot.save()
                                scholarship.montos.transporte = transportation_fun_result 
                                scholarship.montos.save()
                                expense = Gasto_beca.objects.create( estudiante = student_pivot, beca = scholarship, cantidad_dinero = scholarship.auxilio_transporte, tiempo_acumulado =  6, tiempo_seleccionado = "Meses", tipo = 'Transporte')  #Create a expense to One particular Student and save it
                                expense.save()
                            else:
                                scholarship.montos.save()
                                flag = False
                                its_missing += 1 
                        else:
                            counter_students += 1  
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



            
