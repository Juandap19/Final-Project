from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm, FinancialTranspAcademicForm , FinancialTAByStudentForm
from follow_students.models import Scholarship_expense, Student, Scholarship , Major, User
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
        query = Student.objects.filter(code = student_code) # search the student
        if query:
            query = Student.objects.get(code = student_code)
            query1 = Scholarship.objects.get(id = query.scholarship_id)  #Search the scholarship that is associated with the student 
            new_value = float(query1.amount.alimentation) - float(money_quantity)  #Calculate the new value
            if new_value >= 0:
                query1.amount.alimentation = new_value
                query1.amount.save() 
                expense =  Scholarship_expense.objects.create( student = query, money_quantity = money_quantity, accumulated_time =  acumulate_time, selected_time = select_time, type_mount = 'Alimentación', scholarship = query1)  #Create a expense to One particular Student and save it
                expense.save()   #Save the new value in the data base
                messages.success(request,"Proceso completado")
                return HttpResponseRedirect(request.path)   
            else:
                #Case when the Scholarship doesn`t have enought money to pay the new student money quantity`
                money_quantity = query1.amount.alimentation
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
         students_list = Student.objects.all()
         for student_pivot in students_list:
             if student_pivot.aux_academic == "0":
                if student_pivot.scholarship not in missing_scholarship:
                    missing_scholarship.append(student_pivot.scholarship)
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
            student = Student.objects.filter(code = student_form )
            if student:
                student = Student.objects.get(code = student_form )
                scholarship = student.scholarship
                academic_fun_result = round(student.major.price * (scholarship.academic_percentage/100))
                if student.aux_academic == "0":
                    if academic_fun_result >= 0:
                        student.aux_academic  = "1"
                        student.save()
                        scholarship.amount.academic = academic_fun_result 
                        scholarship.amount.save()
                        expense = Scholarship_expense.objects.create( student = student, scholarship = scholarship, money_quantity = academic_fun_result, accumulated_time =  6, selected_time = "Meses", type_mount = 'Academico')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado".format(student.code ))
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
            query = Scholarship.objects.filter(code = scholarship_code)
            if query:
                scholarship = Scholarship.objects.get(code = scholarship_code)
                # Calculate the Major that scholarship gonna pay it
                students_list = Student.objects.filter(scholarship = scholarship).values()
                flag = True
                its_missing = 0
                counter_students = 0
                for student in students_list:
                    major_aux = Major.objects.get(id = student['major_id'] )
                    student_pivot = Student.objects.get(code = student['code'])
                    major_to_add = round(major_aux.price * float(scholarship.academic_percentage/100))
                    result_education_fun = scholarship.amount.academic - major_to_add
                    if student_pivot.aux_academic == "0":
                        if result_education_fun >= 0:
                            student_pivot.aux_academic = "1"
                            student_pivot.save()
                            scholarship.amount.academic  = result_education_fun 
                            scholarship.amount.save()
                            expense = Scholarship_expense.objects.create( student = student_pivot, scholarship = scholarship, money_quantity = major_to_add, accumulated_time =  6, selected_time = "Meses", type_mount = 'Académico')  #Create a expense to One particular Student and save it
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
        students_list = Student.objects.all()
        for student_pivot in students_list:
            if student_pivot.aux_transportation == "0":
                if student_pivot.scholarship not in missing_scholarship:
                    missing_scholarship.append(student_pivot.scholarship)
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
            student = Student.objects.filter(code = student_form )
            if student:
                student = Student.objects.get(code = student_form )
                scholarship = student.scholarship
                transportation_fun_result = scholarship.amount.transport - scholarship.transportation
                if student.aux_transportation == "0":
                    if transportation_fun_result >= 0:
                        student.aux_transportation  = "1"
                        student.save()
                        scholarship.amount.transporte = transportation_fun_result 
                        scholarship.amount.save()
                        expense = Scholarship_expense.objects.create( student = student, scholarship = scholarship, money_quantity = scholarship.transportation, accumulated_time =  6, selected_time = "Meses", type_mount = 'Transporte')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado".format(student))
                        return HttpResponseRedirect(request.path) 
                    else:
                        messages.warning(request,"Pago no aprobado Fondos insuficientes de la beca")
                        return HttpResponseRedirect(request.path)
                else:
                    messages.info(request,"El estudiante asociado con el codigo {} ya ha sido pagado previamente".format(student.code))
                    return HttpResponseRedirect(request.path) 
            else:
                messages.error(request,"No existe el codigo {} en el sistema de becados".format(student_form))
                return HttpResponseRedirect(request.path)  
        else:
                scholarship_code = request.POST['scholarship_code']
                query = Scholarship.objects.filter(code = scholarship_code)
                if query:
                    scholarship = Scholarship.objects.get(code = scholarship_code)
                    # Calculate the Transportation that scholarship gonna pay it
                    students_list = Student.objects.filter(scholarship = scholarship).values()
                    flag = True
                    its_missing = 0
                    counter_students = 0
                    for student in students_list:
                        student_pivot = Student.objects.get(code = student['code'])
                        transportation_fun_result = scholarship.amount.transport - scholarship.transportation
                        if student_pivot.aux_transportation == "0": 
                            if  transportation_fun_result >= 0:
                                student_pivot.aux_transportation  = "1"
                                student_pivot.save()
                                scholarship.amount.transporte = transportation_fun_result 
                                scholarship.amount.save()
                                expense = Scholarship_expense.objects.create( student = student_pivot, scholarship = scholarship, money_quantity = scholarship.transportation, accumulated_time =  6, selected_time = "Meses", type_mount = 'Transporte')  #Create a expense to One particular Student and save it
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



            
