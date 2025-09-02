from django.shortcuts import render
from .models import Products, Category

# Create your views here.
def home(request):

    return render(request, "index.html")

def products(request):
    all_products = Products.objects.all()
    return render(request, "products.html", {"all_products": all_products})

def category(request):
    return render(request, "category.html")