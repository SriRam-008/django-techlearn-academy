from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    duration = models.CharField(max_length=50)
    course_image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.course_name

class TrainerModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=20)
    trainer_photo = models.ImageField(upload_to='trainers/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class StudentModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(CourseModel,on_delete=models.SET_NULL,blank=True,null=True)
    trainer = models.ForeignKey(TrainerModel,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'