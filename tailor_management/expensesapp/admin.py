from django.contrib import admin
from expensesapp.models import expense
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class expenseAdmin(ImportExportModelAdmin):
    list_display = ('expense_date','expense_category','expense_amount','description')
admin.site.register(expense,expenseAdmin)