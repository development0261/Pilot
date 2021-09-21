from django.contrib import admin
from .models import Course


# Register your models here.

class extra_course(admin.ModelAdmin):
    list_display = ['course_title', 'course_start_date', 'course_end_date', 'status']


admin.site.register(Course, extra_course)
