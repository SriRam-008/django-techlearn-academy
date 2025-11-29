from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, StudentForm, TrainerForm
from .models import CourseModel,TrainerModel,StudentModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Registration Successful')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print('Login Successful')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

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

def coursedetails_view(request,id):
    course = get_object_or_404(CourseModel,id=id)
    context = {
        'course':course
    }
    return render(request,'coursedetails.html',context)

@login_required
@permission_required('academy.add_coursemodel',raise_exception=True)
def addcourse_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Course added successfully')
            return redirect('courses')
        else:
            print(form.errors)
    else:
        form = CourseForm()
    context = {
        'form':form
    }
    return render(request,'addcourse.html',context)

@login_required
@permission_required('academy.change_coursemodel',raise_exception=True)
def updatecourse_view(request,id):
    course = get_object_or_404(CourseModel,id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
            print('Course updated successfully')
            return redirect('courses')
        else:
            print(form.errors)
    else:
        form = CourseForm(instance=course)
    context = {
        'form':form,
        'course':course   
    }
    return render(request,'updatecourse.html',context)

@login_required
@permission_required('academy.delete_coursemodel',raise_exception=True)
def deletecourse_view(request,id):
    course = get_object_or_404(CourseModel,id=id)
    course.delete()
    print('Course deleted successfully')
    return redirect('courses')

def trainers_view(request):
    trainers = TrainerModel.objects.all()
    context = {
        'trainers':trainers,
    }
    return render(request,'trainers.html',context)

@login_required
def trainerdetailes_view(request,id):
    trainer = get_object_or_404(TrainerModel,id=id)
    context = {
        'trainer':trainer
    }
    return render(request,'trainerdetails.html',context)

@login_required
@permission_required('academy.add_trainermodel',raise_exception=True)
def addtrainer_view(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Trainner added successfully')
            return redirect('trainers')
        else:
            print(form.errors)
    else:
        form = TrainerForm()
    context = {
        'form':form
    }
    return render(request,'addtrainer.html',context)

@login_required
@permission_required('academy.change_trainermodel',raise_exception=True)
def updatetrainer_view(request,id):
    trainer = get_object_or_404(TrainerModel,id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            print('Trainer updated successfully')
            return redirect('trainers')
        else:
            print(form.errors)
    else:
        form = TrainerForm(instance=trainer)
    context = {
        'form':form,
        'trainer':trainer   
    }
    return render(request,'updatetrainer.html',context)

@login_required
@permission_required('academy.delete_trainermodel',raise_exception=True)
def deletetrainer_view(request,id):
    trainer = get_object_or_404(TrainerModel,id=id)
    trainer.delete()
    print('Trainer deleted successfully')
    return redirect('trainers')

def students_view(request):
    students = StudentModel.objects.all()
    context = {
        'students':students
    }
    return render(request,'students.html',context)

@login_required
@permission_required('academy.view_studentmodel',raise_exception=True)
def studentdetails_view(request,id):
    student = get_object_or_404(StudentModel,id=id)
    context = {
        'student':student
    }
    return render(request,'studentdetails.html',context)

@login_required
@permission_required('academy.add_studentmodel',raise_exception=True)
def addstudent_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Student added successfully')
            return redirect('students')
        else:
            print(form.errors)
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request,'addstudent.html',context)

@login_required
@permission_required('academy.change_studentmodel',raise_exception=True)
def updatestudent_view(request,id):
    student = get_object_or_404(StudentModel,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            print('Student Updated successfully')
            return redirect('students')
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=student)
    context = {
        'form':form,
        'student':student
    }
    return render(request,'updatestudent.html',context)

@login_required
@permission_required('academy.delete_studentmodel',raise_exception=True)
def deletestudent_view(request,id):
    student = get_object_or_404(StudentModel,id=id)
    student.delete()
    print('Student deleted successfully')
    return redirect('students')

