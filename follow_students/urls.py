# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.dashboard import Dashboard
from follow_students.views.uploadCREA import Upload_dataCREA

urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('dashboard', Dashboard.as_view()),
    path('uploadCREA', Upload_dataCREA.as_view())
]