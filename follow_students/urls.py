# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.dashboard import Dashboard
from follow_students.views.menuReport import MenuReport
from follow_students.views.generateReport import GenerateReport
from follow_students.views.upload_data import Upload_dataPD
from follow_students.views.student_manage import StudentManage
from follow_students.views.student_edit import StudentEdit
from follow_students.views.registroEstudiantes import RegistroEstudiantes
from follow_students.views.asignarBeca import AsignarBeca

urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('dashboard/', Dashboard.as_view()),
    path('menuReport/', MenuReport.as_view(), name="menuR"),
    path('generateReport/<int:codigo>/', GenerateReport.as_view(), name="report"),
    path('generateReport/', GenerateReport.as_view(), name="generateR")
    path('upload_dataPD/', Upload_dataPD.as_view(), name = "uploadPD"),
    path('studentManage/', StudentManage.as_view(), name = "studentManage"),
    path('studentManage/studentEdit/<int:pk>/', StudentEdit.as_view(), name = "studentEdit"),
    path('registroEstudiantes/', RegistroEstudiantes.as_view()),
    path('asignarBeca/<str:codigo>/', AsignarBeca.as_view(), name='asignar_beca'),
    path('dashboard/', Dashboard.as_view(), name='dashboard')

]