
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.log_in, name = 'log_in'),
    path('post_log/', views.post_log),
    path('sign_up/', views.sign_up),
    path('logout/', views.signout, name = 'logout'),
]
