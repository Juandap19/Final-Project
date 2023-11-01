
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Notification




class Notifications(View):
 
  def get(self, request):
        notification=Notification.objects.all()[::-1]
        return render(request, 'notification.html', {
            "notifications" : notification
        })
        
  def post(self, request):
         if request.method == 'POST':
          notification=Notification.objects.all()
          notification.update(state=False)
        
         return redirect("/notification")