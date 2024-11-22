from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=50)
    customer_address = models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.customer_name
    
    