# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.dashboard import Dashboard
from follow_students.views.student_manage import StudentManage
from follow_students.views.student_edit import StudentEdit
from follow_students.views.registroEstudiantes import RegistroEstudiantes
from follow_students.views.asignarBeca import AsignarBeca


urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('studentManage/', StudentManage.as_view(), name = "studentManage"),
    path('studentManage/studentEdit/<int:pk>/', StudentEdit.as_view(), name = "studentEdit"),
    path('registroEstudiantes/', RegistroEstudiantes.as_view()),
    path('asignarBeca/<str:codigo>/', AsignarBeca.as_view(), name='asignar_beca'),
    path('dashboard/', Dashboard.as_view(), name='dashboard')
]