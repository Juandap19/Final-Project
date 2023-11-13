from django import forms
from follow_students.models import SupportCenter

class RegisConsult(forms.Form):
    student_code = forms.CharField(max_length=10)
    support_center = forms.ModelChoiceField(queryset=SupportCenter.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
    outcome = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'style': 'resize: none;'})
    )
