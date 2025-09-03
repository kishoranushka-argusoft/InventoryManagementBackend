from django.shortcuts import render, get_object_or_404
from .models import Products, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})

def products(request):
    all_products = Products.objects.all()
    return render(request, "products.html", {"all_products": all_products})

def categories(request):
    return render(request, "category.html")

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, "category_detail.html", {"category": category})

def sellers(request):
    return render(request, "sellers.html")

def transactions(request):
    return render(request, "transactions.html")