from django.contrib import admin
from customers.models import Customer
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class customerAdmin(ImportExportModelAdmin):
    list_display=('customer_name','customer_contact','customer_address')
admin.site.register(Customer, customerAdmin)

