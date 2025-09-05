from django import forms
from .models import Products, Category, Transactions, Sellers


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class AddProductForm(forms.ModelForm):
    # category = forms.CharField()
    # seller = forms.CharField()
    class Meta:
        model = Products
        fields = ['id', 'name', 'image', 'price', 'weight','quantity_in_stock', 'expiry_date', 'category', 'seller']

    # def clean_category(self):
    #     category_name = self.cleaned_data['category']
    #     category, created = Category.objects.get_or_create(name=category_name)
    #     print("&&&&&&&&&&&&&&&&&&&&&&&", category)
    #     return category
    
    # def clean_seller(self):
    #     seller_name = self.cleaned_data['seller']
    #     seller = Sellers.objects.get_or_create(name=seller_name)
    #     return seller
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['transactions_type','product', 'quantity', 'price_per_unit', 'total_price']