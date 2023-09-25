from django.urls import path
from django.contrib import admin
# from follow_students.views.(name) import (name) || Here the views are added from the views folder

urlpatterns = [
    path('admin/', admin.site.urls),
    # Here the paths are added
]