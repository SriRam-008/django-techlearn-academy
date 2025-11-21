from django.shortcuts import render
from .models import CourseModel,TrainerModel,StudentModel

# Create your views here.
def home_view(request):
    total_courses = CourseModel.objects.all().count()
    total_trainers = TrainerModel.objects.all().count()
    total_students = StudentModel.objects.all().count()
    context ={
        'total_courses':total_courses,
        'total_trainers':total_trainers,
        'total_students':total_students
    }
    return render(request,'home.html',context)

def courses_view(request):
    courses = CourseModel.objects.all()
    context = {
        'courses':courses,
    }
    return render(request,'courses.html',context)

def trainers_view(request):
    trainers = TrainerModel.objects.all()
    context = {
        'trainers':trainers,
    }
    return render(request,'trainers.html',context)

def students_view(request):
    students = StudentModel.objects.all()
    context = {
        'students':students
    }
    return render(request,'students.html',context)