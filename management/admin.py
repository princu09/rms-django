from django.contrib import admin
from .models import  *
from import_export.admin import ImportExportModelAdmin

@admin.register(Member)
@admin.register(Maintenance)
@admin.register(Notice)
@admin.register(Gallery)
class ModelAdmin(ImportExportModelAdmin):
       pass