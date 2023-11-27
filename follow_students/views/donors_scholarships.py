from django.views import View
from django.shortcuts import render
from follow_students.models import Scholarship, Donor

class DonorAndScholarships(View):
    def get(self, request):

        scholarship = Scholarship.objects.all()
        donor = Donor.objects.all()

        return render(request, 'donorsAndScholarships.html', {
            'scholarships': scholarship,
            'donors': donor,
        })