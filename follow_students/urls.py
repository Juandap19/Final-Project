# from follow_students.views.(name) import (name) || Here the views are added from the views folder
from django.urls import path
from django.contrib import admin
from follow_students.views.signin import Signin
from follow_students.views.dashboard import Dashboard

urlpatterns = [
    # Here the paths are added
    path('', Signin.as_view()),
    path('dashboard', Dashboard.as_view())
]