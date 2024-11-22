from django.db import models

# Create your models here.
class expense(models.Model):
    expense_date = models.DateField( null=True)
    expense_category = models.CharField(max_length=100, null=True)
    expense_amount = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)