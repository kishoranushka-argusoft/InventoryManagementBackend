from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False) 
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE )

    def __str__(self):
        return self.name

