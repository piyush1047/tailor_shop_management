from django.contrib import admin
from revenueapp.models import revenuedetails
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class revenuedetailsAdmin(ImportExportModelAdmin):
    list_display = ('income_date','income_category','income_amount','description')
admin.site.register(revenuedetails,revenuedetailsAdmin)