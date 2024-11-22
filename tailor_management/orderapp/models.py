from django.db import models
from customers.models import Customer


# Create your models here.

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('Topwear','Topwear'),
        ('Bottomwear','Bottomwear'),
        ('Top-Bottom','Top-Bottom'),
    ]
    
    order_name = models.CharField(max_length=100,null=True, blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=100,  null=True)
    order_date = models.CharField(max_length=100,  null=True)
    deliver_date = models.DateField( null=True)
    priority = models.CharField(max_length=100,  null=True)
    Total_payment = models.CharField(max_length=100,  null=True)
    Advance_Payment= models.CharField(max_length=100,  null=True)
    due_payment = models.CharField(max_length=100,  null=True)
    quantity= models.CharField(max_length=100,  null=True)
    product_img=models.FileField(upload_to="images/",max_length=250,null=True,default=None)
    garment_type = models.CharField(max_length=100, choices=ORDER_TYPE_CHOICES, null=True)

    
    
    # Measurements for shirt
    neck_size = models.CharField(max_length=50,  null=True, blank=True)
    chest_size = models.CharField(max_length=50,  null=True, blank=True)
    sleeve_length = models.CharField(max_length=50,  null=True, blank=True)
    shirt_length = models.CharField(max_length=50,null=True, blank=True)
    stomach = models.CharField(max_length=50, null=True, blank=True)
    heap = models.CharField(max_length=50,null=True, blank=True)
    shoulder = models.CharField(max_length=50,null=True, blank=True)
    remark_shirt = models.CharField(max_length=50,null=True, blank=True)


    # Measurements for pant
    waist_size = models.CharField(max_length=50,  null=True, blank=True)
    length_size = models.CharField(max_length=50,  null=True, blank=True)
    pant_heap = models.CharField(max_length=50,null=True, blank=True)
    heap_loosing = models.CharField(max_length=50,null=True, blank=True)
    mohri = models.CharField(max_length=50,null=True, blank=True)
    thai = models.CharField(max_length=50,null=True, blank=True)
    Knee_Size = models.CharField(max_length=50,null=True, blank=True)
    langot = models.CharField(max_length=50,null=True, blank=True)
    pindli = models.CharField(max_length=50,null=True, blank=True)
    remark = models.CharField(max_length=50,null=True, blank=True)

    
    def _str_(self):
        return self.order_name
    
    def _str_(self):
        return self.customer