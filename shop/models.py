# models.py
from django.db import models
import uuid
from django.utils import timezone



class Product(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    buy_price = models.CharField(max_length=50)
    min_price = models.FloatField(max_length=50)

    def __str__(self):
        return self.name

class Sale(models.Model):
    CHOICES = [
        ('cash', 'cash'),
        ('mpesa', 'mpesa'),
        ('co-op', 'co-op'),
    ]
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=10, choices=CHOICES)
    sold_price = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.code)

    
