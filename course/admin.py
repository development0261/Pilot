from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Course, City


# Register your models here.
class extra_course(admin.ModelAdmin):
    list_display = [
        "course_city",
        "course_title",
        "course_start_date",
        "course_end_date",
        "status",
    ]


@admin.register(City)
class PersonAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Course, extra_course)
