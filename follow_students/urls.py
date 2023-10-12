# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.upload_dataBU import Upload_dataBU
from follow_students.views.dashboard import Dashboard

from follow_students.views.financial import FinancialSupport, FinancialAcademic , FinancialTransport

from follow_students.views.request_update import RequestUpd
from follow_students.views.upload_dataCREA import Upload_dataCREA
from follow_students.views.menuReport import MenuReport
from follow_students.views.generateReport import GenerateReport
from follow_students.views.upload_dataPD import Upload_dataPD
from follow_students.views.student_manage import StudentManage
from follow_students.views.student_edit import StudentEdit
from follow_students.views.registroEstudiantes import RegistroEstudiantes
from follow_students.views.asignarBeca import AsignarBeca



urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('apoyo_financiero_alimentacion/', FinancialSupport.as_view(), name = 'alimentationExp' ),
    path('apoyo_financiero_academico/', FinancialAcademic.as_view() , name = 'educationExp'),
    path('apoyo_financiero_transporte/', FinancialTransport.as_view() , name = 'transportExp'),
    path('requestupd', RequestUpd.as_view(), name = "requestUpdate"),
    path('dashboard/', Dashboard.as_view()),
    path('menuReport/', MenuReport.as_view(), name="menuR"),
    path('generateReport/<int:codigo>/', GenerateReport.as_view(), name="report"),
    path('generateReport/', GenerateReport.as_view(), name="generateR"),
    path('upload_dataPD/', Upload_dataPD.as_view(), name = "uploadPD"),
    path('studentManage/', StudentManage.as_view(), name = "studentManage"),
    path('studentManage/studentEdit/<int:pk>/', StudentEdit.as_view(), name = "studentEdit"),
    path('registroEstudiantes/', RegistroEstudiantes.as_view()),
    path('asignarBeca/<str:codigo>/', AsignarBeca.as_view(), name='asignar_beca'),
    path('upload_dataCREA/', Upload_dataCREA.as_view(), name = "uploadCREA"),
    path('upload_dataBU/', Upload_dataBU.as_view(), name = "uploadBU")

]