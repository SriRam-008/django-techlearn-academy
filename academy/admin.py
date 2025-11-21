from django.contrib import admin

from .models import CourseModel, StudentModel, TrainerModel

#Admain Page Customization 
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','description','duration']
    search_fields = ['course_name','description']
    list_filter = ['course_name','duration']
    ordering = ['id']
    list_display_links = ['course_name']
    list_editable = ['description','duration']

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','expertise']
    search_fields = ['first_name','last_name','email']
    list_filter = ['expertise']
    ordering = ['id']
    list_display_links = ['full_name']
    list_editable = ['expertise','email']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','is_active','enrolled_course','trainer']
    search_fields = ['first_name','last_name','email']
    list_filter = ['enrolled_course','is_active']
    ordering = ['id']
    list_display_links = ['full_name']
    list_editable = ['email','is_active','trainer','enrolled_course']


#Models
admin.site.register(CourseModel,CourseAdmin)
admin.site.register(TrainerModel,TrainerAdmin)
admin.site.register(StudentModel,StudentAdmin)