from django.contrib import admin
from .models import Category, Products, Sellers, Transactions

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sellers)
admin.site.register(Transactions)