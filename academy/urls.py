from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('courses/',views.courses_view,name='courses'),
    path('course/<int:id>',views.coursedetails_view,name='coursedetails'),
    path('addcourse/',views.addcourse_view,name='addcourse'),
    path('updatecourse/<int:id>',views.updatecourse_view,name='updatecourse'),
    path('deletecourse/<int:id>',views.deletecourse_view,name='deletecourse'),
    path('trainers/',views.trainers_view,name='trainers'),
    path('trainer/<int:id>',views.trainerdetailes_view,name='trainerdetails'),
    path('addtrainer/',views.addtrainer_view,name='addtrainer'),
    path('updatetrainer/<int:id>',views.updatetrainer_view,name='updatetrainer'),
    path('dalatetrainer/<int:id>',views.deletetrainer_view,name='deletetrainer'),
    path('students/',views.students_view,name='students'),
    path('student/<int:id>',views.studentdetails_view,name='studentdetails'),
    path('addstudent/',views.addstudent_view,name='addstudent'),
    path('updatestudent/<int:id>',views.updatestudent_view,name='updatestudent'),
    path('deletestudent/<int:id>',views.deletestudent_view,name='deletestudent'),

]