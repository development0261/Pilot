from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Course, City, Batch


@admin.register(City)
class PersonAdmin(ImportExportModelAdmin):
    pass


class Extra_Course(admin.ModelAdmin):
    list_display = [
        "course_city",
        "course_title"
    ]
    list_filter = [
        "course_city"
    ]

class Extra_Batch(admin.ModelAdmin):
    list_display = [
        "batch_city",
        "batch_start_date",
        "batch_end_date",
        "batch_status",
    ]

    readonly_fields = [
        "batch_status",
    ]


admin.site.register(Course,Extra_Course)
admin.site.register(Batch, Extra_Batch)
