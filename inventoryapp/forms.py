from django import forms
from .models import Products, Category

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['id', 'name', 'image', 'price', 'weight','quantity_in_stock', 'expiry_date', 'category']
        