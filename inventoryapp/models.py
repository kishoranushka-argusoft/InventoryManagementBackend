from django.db import models
from django.utils import timezone
from django.db.models import F



# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField( default=timezone.now)
    image = models.ImageField(upload_to='category_images/', default='photos/rice.png')

    def __str__(self):
        return self.name
    
class Sellers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(null=False)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False) 
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    expiry_date = models.DateTimeField()
    image = models.ImageField(upload_to='product_images/', default='photos/rice.png')
    quantity_in_stock = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField( default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1 )
    seller = models.ManyToManyField(Sellers )

    def __str__(self):
        return self.name
    

class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICE =[
        ('P', 'Purchase'),
        ('S', 'Sale'),
        ('R', 'Return'),
    ]

    id= models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    transactions_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICE)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total_price = models.GeneratedField(
        expression=F("quantity") * F("price_per_unit"),
        output_field=models.DecimalField(max_digits=10, decimal_places=2),
        db_persist=True,
    )
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.transactions_type


