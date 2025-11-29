from django import forms
from .models import CourseModel, StudentModel, TrainerModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model = TrainerModel
        fields = '__all__'   

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'  