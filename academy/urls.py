from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('courses/',views.courses_view,name='courses'),
    path('trainers/',views.trainers_view,name='trainers'),
    path('students/',views.students_view,name='students'),

]