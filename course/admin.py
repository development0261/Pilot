from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Course, City, Batch


@admin.register(City)
class PersonAdmin(ImportExportModelAdmin):
    pass


class Extra_Batch(admin.ModelAdmin):
    list_display = ["batch_city", "batch_start_date", "batch_end_date", "batch_status"]


admin.site.register(Course)
admin.site.register(Batch,Extra_Batch)
