# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.dashboard import Dashboard
from follow_students.views.menuReport import MenuReport
from follow_students.views.generateReport import GenerateReport



urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('dashboard/', Dashboard.as_view()),
    path('menuReport/', MenuReport.as_view(), name="menuR"),
     path('generateReport/<int:codigo>/', GenerateReport.as_view(), name="report"),
    path('generateReport/', GenerateReport.as_view(), name="generateR")
]