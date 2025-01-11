from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ratings = models.FloatField(default=0.0) 
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name