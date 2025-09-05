from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category, Sellers, Transactions
from .forms import AddCategoryForm, AddProductForm, TransactionForm
from django.contrib import messages

# Create your views here.
def home(request):
    categories = Category.objects.all()
    all_products = Products.objects.all()

    return render(request, "index.html", {"categories": categories, "all_products":all_products})

def products(request):
    all_products = Products.objects.all()
    return render(request, "products.html", {"all_products": all_products})

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit= False)
            # product.category = form.cleaned_data['category']
            product.save()
            return redirect('add_product')
        
    else:
        form = AddProductForm()
    return render(request, "add_product.html", {'form':form})

def product_edit(request, product_id):
    product = get_object_or_404(Products, pk = product_id)
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products')
        
    else:
        form = AddProductForm(instance=product)

    return render(request, "add_product.html", {'form': form})


def product_delete(request, product_id):
    product = get_object_or_404(Products, pk= product_id)
    if request.method == "POST":
        product.delete()
        return redirect('home')
    
    return render (request, "confirm_delete.html", {"product":product})

def categories(request):
    categories = Category.objects.all()
    return render(request, "category.html", {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category =form.save(commit=False)
            # category.user == request.user
            category.save()
            return redirect('add_category')
    else:
        form = AddCategoryForm()
    return render(request, "add_category.html", {'form':form})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, "category_detail.html", {"category": category})


def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category= form.save(commit=False)
            category.save()
            return redirect('categories')
        
    else:
        form = AddCategoryForm(instance=category)

    return render(request, 'add_category.html', {'form':form})

def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method=='POST':
        category.delete()
        return redirect('categories')

    return render(request, 'confirm_delete.html', {"category":category})

def sellers(request):
    sellers = Sellers.objects.all()
    return render(request, "sellers.html", {"sellers":sellers})

def transactions_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, request.FILES)
        print("🐍 File: inventoryapp/views.py | Line: 105 | transactions ~ form",form)
        transactions = form.save(commit=False)
        
        if form.is_valid():
            print("----------------------------------", transactions)
            product = transactions.product
            print("++++++++++++++++++++++++",product)
            transactions.price_per_unit = product.price
            print("^^^^^^^^^^^^^^^^^^^^^^^^^", transactions.price_per_unit)
            transactions.total_price = transactions.quantity* transactions.price_per_unit
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$", transactions.total_price)

            if transactions.transactions_type == 'sale':
                if product.quantity_in_stock >= transactions.quantity:
                    product.quantity_in_stock -= transactions.quantity
                    product = form.save(commit=False)
                    product.save()
                    transactions = form.save(commit=False)
                    transactions.save()
                    messages.success(request, "sell done successfully")

                else:
                    messages.error(request,"Not enough stock available!")

            elif transactions.transactions_type =='Return':
                product.quantity_in_stock += transactions.quantity
                product = form.save(commit=False)
                product.save()
                transactions = form.save(commit=False)
                transactions.save()
                messages.success(request, "return stock added successfully")
                return redirect ('transactions_view')

    else:
        form = TransactionForm()
    return render(request, "transactions.html", {'form':form})
    
    

def sell(request):
    return render(request, 'sell.html')

def sell_return(request):
    return render(request, 'sell_return.html')
