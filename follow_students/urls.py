# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.views.defaults import page_not_found
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.upload_dataBU import Upload_dataBU
from follow_students.views.dashboard import Dashboard
from follow_students.views.logout import Logout
from follow_students.views.financial import FinancialSupport, FinancialAcademic , FinancialTransport
from follow_students.views.request_update import RequestUpd
from follow_students.views.upload_dataCREA import Upload_dataCREA
from follow_students.views.menuReport import MenuReport
from follow_students.views.generateReport import GenerateReport
from follow_students.views.upload_dataPD import Upload_dataPD
from follow_students.views.student_manage import StudentManage
from follow_students.views.student_edit import StudentEdit
from follow_students.views.studentsRegister import StudentsRegister
from follow_students.views.assignScholarship import AssignScholarship
from follow_students.views.generate_pdf import GeneratePDF
from follow_students.views.menuCancelation import MenuCancelation
from follow_students.views.cancelationSection import CancelationSection
from follow_students.views.notification import Notifications
from follow_students.views.goalEvaluation import GoalEvaluation
from follow_students.views.donors_scholarships import DonorAndScholarships

urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view(), name = "signin"),
    path('apoyo_financiero_alimentacion/', FinancialSupport.as_view(), name = 'alimentationExp' ),
    path('apoyo_financiero_academico/', FinancialAcademic.as_view() , name = 'educationExp'),
    path('apoyo_financiero_transporte/', FinancialTransport.as_view() , name = 'transportExp'),
    path('requestupd/', RequestUpd.as_view(), name = "requestUpdate"),
    path('dashboard/', Dashboard.as_view(), name = 'dashboard'),
    path('menuReport/', MenuReport.as_view(), name="menu_report"),
    path('generateReport/', GenerateReport.as_view(), name="generate_report"),
    path('generate_pdf/<int:code>/', GeneratePDF.as_view(), name='generate_pdf'),
    path('upload_dataPD/', Upload_dataPD.as_view(), name = "uploadPD"),
    path('studentManage/', StudentManage.as_view(), name = "studentManage"),
    path('studentManage/goalEvaluation/<int:pk>/', GoalEvaluation.as_view(), name = "goalEvaluation"),
    path('studentManage/studentEdit/<int:pk>/', StudentEdit.as_view(), name = "studentEdit"),
    path('studentsRegister/', StudentsRegister.as_view()),
    path('assignScholarship/<str:code>/', AssignScholarship.as_view(), name='asignar_scholarship'),
    path('upload_dataCREA/', Upload_dataCREA.as_view(), name = "uploadCREA"),
    path('upload_dataBU/', Upload_dataBU.as_view(), name = "uploadBU"),
    path('menuCancelation/', MenuCancelation.as_view(), name = "MenuC"),
    path('cancelationSection/', CancelationSection.as_view(), name = "CancelationS"),
    path('menuCancelation/<int:code>/', MenuCancelation.as_view(), name="section"),
    path('cancelationSection/<int:code>/', CancelationSection.as_view(), name="cancelation"),
    path('notification/', Notifications.as_view(), name = "notis"),
    path('notification/', Notifications.as_view(), name = "clean"),
    path('donorsAndScholarships/', DonorAndScholarships.as_view(), name = "donorsAndScholarships"),
    path('logout/', Logout.as_view(), name = "logout")
]