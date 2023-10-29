
from django.shortcuts import render
from django.views import View





class CancelationSection (View):

    
    def get(self, request):

        return render(request, 'cancelationSection.html'
        )
    