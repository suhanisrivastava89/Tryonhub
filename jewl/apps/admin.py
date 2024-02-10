from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product
from .models import MainProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display= ('Type','Material','Cost','Design', 'Image' )


@admin.register(MainProduct)
class ProductAdmin(ImportExportModelAdmin):
    list_display= ('Type','Material','Cost','Design', 'Image' )