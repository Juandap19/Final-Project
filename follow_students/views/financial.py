from django.views import View
from django.shortcuts import render
from follow_students.forms.financial_form import FinancialForm, FinancialTranspAcademicForm , FinancialTAByStudentForm
from follow_students.models import Scholarship_expense, Student, Scholarship , Major, User , Notification
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage

class FinancialSupport(View):
    def get(self, request):
        return render(request, './financial_alimentation.html', {
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

                # Notificate the donor and philanthropy.
                if(query1.amount.alimentation <= 1000000):
                    recipient = query1.donor.mail
                    subject = "Agotamiento de Recursos Alimentarios"
                    message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se estan acabando los recursos de alimentacíon utiles.".format( query1.name, query1.code, query1.donor.name)
                    from_email = "sistemaApoyoFinanciero@gmail.com" 

                    email = EmailMessage(subject, message, from_email, [recipient]) 
                    email.send()
                    notification = Notification(name="Cuidado", student= query , description=" Se estan Acabando los recursos utiles de Alimentación para la Beca Asociada al estudiante")
                    notification.save()
                
                return HttpResponseRedirect(request.path, status = 200)   
            else:
                #Case when the Scholarship doesn`t have enought money to pay the new student money quantity`
                money_quantity = query1.amount.alimentation
                query1.amount.save()
                new_value = abs(new_value)
                messages.warning(request,"Fondos insuficientes de alimentación para registrar el pago")

                recipient = query1.donor.mail
                subject = "Se Acabaron los recursos Alimentarios"
                message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se estan acabando los recursos de alimentacíon utiles.".format( query1.name, query1.code, query1.donor.name)
                from_email = "sistemaApoyoFinanciero@gmail.com"
                email = EmailMessage(subject, message, from_email, [recipient]) 
                email.send()
                notification = Notification(name="Peligro", student= query, description="Se  Acabaron los recursos utiles de Alimentacion  para la Beca Asociada al estudiante")
                notification.save()
                return  HttpResponseRedirect(request.path)   
        else:
            messages.error(request,"El codigo del estudiante {}  no existe ".format( student_code ))
            return HttpResponseRedirect(request.path)
        
    
class FinancialAcademic(View):
    def get(self, request):
         missing_scholarship = []        
         students_list = Student.objects.all()
         students_missing = []
         for student_pivot in students_list:
             if student_pivot.aux_academic == "0":
                students_missing.append(student_pivot)
                if student_pivot.scholarship:
                    if student_pivot.scholarship not in missing_scholarship:
                        missing_scholarship.append(student_pivot.scholarship)
        
         students_list = Student.objects.all().values_list('code', flat=True)
         scholarship_list = Scholarship.objects.all().values_list('code', flat=True)
         return render(request, './financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Académico",
            'becas_faltantes': missing_scholarship,
            'student_form': FinancialTAByStudentForm(),
            'students_missing': students_missing,
            'all_students': students_list,
            'all_scholarships': scholarship_list
        })
    
    def post(self, request):
        student_form = request.POST.get('student_code')
        if student_form:
            student = Student.objects.filter(code = student_form )
            if student:
                student = Student.objects.get(code = student_form )
                scholarship = student.scholarship
                academic_fun_result = student.scholarship.amount.academic - round(student.major.price * (scholarship.academic_percentage/100))
                if student.aux_academic == "0":
                    if academic_fun_result >= 0:
                        student.aux_academic  = "1"
                        student.save()
                        scholarship.amount.academic = academic_fun_result 
                        scholarship.amount.save()
                        expense = Scholarship_expense.objects.create( student = student, scholarship = scholarship, money_quantity = academic_fun_result, accumulated_time =  6, selected_time = "Meses", type_mount = 'Academico')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado".format(student.code ))
                        # Notificate the donor and philanthropy.
                        if(scholarship.amount.academic < 10000000):
                            recipient = scholarship.donor.mail
                            subject = "Agotamiento de Recursos Academicos"
                            message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {}  pertence como donante, se están acabando los recursos de Academicos.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                            from_email = "sistemaApoyoFinanciero@gmail.com"
                            email = EmailMessage(subject, message, from_email, [recipient]) 
                            email.send()
                            notification = Notification(name="Cuidado", student= student , description=" Se le estan Acabando los recursos Academicos para la Beca Asociada al estudiante")
                            notification.save()
                        return HttpResponseRedirect(request.path) 
                    else:
                        messages.warning(request,"Pago no aprobado Fondos insuficientes de la beca")
                        recipient = scholarship.donor.mail
                        subject = "Peligro"
                        message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {}pertence como donante, se le acabaron los recursos de Academicos utiles.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                        from_email = "sistemaApoyoFinanciero@gmail.com"
                        email = EmailMessage(subject, message, from_email, [recipient]) 
                        email.send()
                        notification = Notification(name="Peligro", student= student , description=" Se le estan Acabando los recursos Academicos para la Beca Asociada al estudiante")
                        notification.save()
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
                            
                            # Notificate the donor and philanthropy.
                            if(scholarship.amount.academic < 10000000):
                                recipient = scholarship.donor.mail
                                subject = "Agotamiento de Recursos Academicos"
                                message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se le estan acabando los recursos de Academicos utiles.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                                from_email = "sistemaApoyoFinanciero@gmail.com"
                                email = EmailMessage(subject, message, from_email, [recipient]) 
                                email.send()
                                notification = Notification(name="Cuidado", student= student_pivot , description=" Se estan Acabando los recursos Academicos para la Beca Asociada al estudiante")
                                notification.save()
                            
                        else:
                            scholarship.amount.save()
                            flag = False
                            its_missing += 1 
                    else:
                        counter_students += 1     
                if flag:
                    if counter_students != len(students_list):
                        messages.success(request,"Proceso completado")
                        return HttpResponseRedirect(request.path )
                else:
                    messages.warning(request,"Fondos insuficientes faltan: {} estudiantes por matricular".format(its_missing))
                    recipient = scholarship.donor.mail
                    subject = "Peligro"
                    message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se le acabaron los recursos Academicos utiles.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                    from_email = "sistemaApoyoFinanciero@gmail.com"
                    email = EmailMessage(subject, message, from_email, [recipient]) 
                    email.send()
                    notification = Notification(name="Peligro", student= student_pivot , description=" Se le estan Acabando los recursos Academicos utiles para la Beca Asociada al estudiante")
                    notification.save()
                    return HttpResponseRedirect(request.path)

class FinancialTransport(View):
    def get(self, request):
        missing_scholarship = []        
        students_list = Student.objects.all()
        students_missing = []
        for student_pivot in students_list:
            if student_pivot.aux_transportation != "4":
                print(student_pivot.aux_transportation)
                students_missing.append(student_pivot)
                if student_pivot.scholarship not in missing_scholarship:
                    missing_scholarship.append(student_pivot.scholarship)

                    
        return render(request, './financial_education_transportation.html', {
            'form': FinancialTranspAcademicForm(),
            'error': False,
            'main_title': "Pago Transporte",
            'becas_faltantes': missing_scholarship,
            'student_form': FinancialTAByStudentForm(),
            'students_missing': students_missing,
        })
    
    def post(self, request):
        student_form = request.POST.get('student_code')
        if student_form:
            student = Student.objects.filter(code = student_form )
            if student: 
                student = Student.objects.get(code = student_form )
                scholarship = student.scholarship
                transportation_fun_result = scholarship.amount.transport - scholarship.transportation
                if student.aux_transportation != "4":
                    if transportation_fun_result >= 0:
                        aux_var_transportation =  int(student.aux_transportation)
                        aux_var_transportation += 1
                        student.aux_transportation  = aux_var_transportation
                        student.save()
                        scholarship.amount.transport = transportation_fun_result 
                        scholarship.amount.save()
                        expense = Scholarship_expense.objects.create( student = student, scholarship = scholarship, money_quantity = scholarship.transportation, accumulated_time =  6, selected_time = "Meses", type_mount = 'Transporte')  #Create a expense to One particular Student and save it
                        expense.save()
                        messages.success(request,"Proceso completado")
                        # Notificate the donor and philanthropy.
                        if(scholarship.amount.transport < 5000000):
                            recipient = scholarship.donor.mail
                            subject = "Agotamiento de Recursos de Transporte "
                            message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {}  pertence como donante, se le estan acabando los recursos de Transporte utiles.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                            from_email = "sistemaApoyoFinanciero@gmail.com"
                            email = EmailMessage(subject, message, from_email, [recipient]) 
                            email.send()
                            notification = Notification(name="Cuidado", student= student , description=" Se están Acabando los recursos de Transporte utiles para la Beca Asociada al estudiante")
                            notification.save()

                        return HttpResponseRedirect(request.path) 
                    else:
                        messages.warning(request,"Pago no aprobado Fondos insuficientes de la beca")
                        recipient = scholarship.donor.mail
                        subject = "Se Acabaron los recursos de transporte"
                        message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {}  pertence como donante, se le  acabaron los recursos de Transporte utiles.\n Comunicate con la oficina de Apoyo financiero para mas informacion\n ".format( scholarship.name, scholarship.code, scholarship.donor.name)
                        from_email = "sistemaApoyoFinanciero@gmail.com"
                        email = EmailMessage(subject, message, from_email, [recipient]) 
                        email.send()
                        notification = Notification(name="Peligro", student= student, description=" Se   Acabaron los recursos de Transporte para la Beca Asociada al estudiante")
                        notification.save()
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
                        if student_pivot.aux_transportation != "4": 
                            if  transportation_fun_result >= 0:
                                aux_var_transportation = int(student_pivot.aux_transportation)
                                aux_var_transportation += 1
                                student_pivot.aux_transportation  = aux_var_transportation
                                student_pivot.save()
                                scholarship.amount.transport = transportation_fun_result 
                                scholarship.amount.save()
                                expense = Scholarship_expense.objects.create( student = student_pivot, scholarship = scholarship, money_quantity = scholarship.transportation, accumulated_time =  6, selected_time = "Meses", type_mount = 'Transporte')  #Create a expense to One particular Student and save it
                                expense.save()
                                # Notificate the donor and philanthropy.
                                if(scholarship.amount.transport < 5000000):
                                    recipient = scholarship.donor.mail
                                    subject = "Agotamiento de Recursos de Transporte "
                                    message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se le estan acabando los recursos de Transporte utiles.".format( scholarship.name, scholarship.code, scholarship.donor.name)
                                    from_email = "sistemaApoyoFinanciero@gmail.com"
                                    email = EmailMessage(subject, message, from_email, [recipient]) 
                                    email.send()
                                    notification = Notification(name="Cuidado", student= student , description=" Se estan Acabando los recursos de Transporte utiles para la Beca Asociada al estudiante")
                                    notification.save()

                            else:
                                student = student_pivot
                                scholarship.amount.save()
                                flag = False
                                its_missing += 1 
                        else:
                            counter_students += 1 
                    if flag:
                        if counter_students != len(students_list):
                            messages.success(request,"Proceso completado")
                            return HttpResponseRedirect(request.path)
                    else:
                            messages.warning(request,"Fondos insuficientes faltan: {} estudiantes por auxilio de transporte".format(its_missing))
                            recipient = scholarship.donor.mail
                            subject = "Se Acabaron los recursos de Transporte"
                            message = "Le informamos que La beca {} asociada al codigo {} a la cual usted {} pertence como donante, se le  acabaron los recursos de Transporte utiles.\n Comunicate con la oficina de Apoyo financiero para mas informacion\n ".format( scholarship.name, scholarship.code, scholarship.donor.name)
                            from_email = "sistemaApoyoFinanciero@gmail.com"
                            email = EmailMessage(subject, message, from_email, [recipient]) 
                            email.send()
                            notification = Notification(name="Peligro", student= student, description=" Se  Acabaron los recursos de Transporte para la Beca Asociada al estudiante")
                            notification.save()
                            return HttpResponseRedirect(request.path)



            
