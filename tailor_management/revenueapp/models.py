from django.db import models

# Create your models here.
class revenuedetails(models.Model):
    income_date = models.CharField(max_length=100, null=True)
    income_category=models.CharField(max_length=100, null=True)
    income_amount=models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)