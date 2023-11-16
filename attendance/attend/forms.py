from django import forms
from .models import Student

class YourTaskForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['instructor', 'automation_button_clicked']