from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Student

class GoalEvaluation(View):

    def get(self, request, pk):
        student_with_goals = get_object_or_404(Student, id=pk)
        goals = student_with_goals.get_scholarship_goals()
        has_scholarships = student_with_goals.has_scholarships()

        return render(request, 'goalEvaluation.html', {
            'student': student_with_goals,
            'goals': goals,
            'has_scholarships': has_scholarships,
        })
    
    def post(self, request):

        id = int(request.POST['idStudent'])

        studentWithGoals = Student.objects.get(pk = id)


        return render(request, 'goalEvaluation.html', {
            "student": studentWithGoals,
        })