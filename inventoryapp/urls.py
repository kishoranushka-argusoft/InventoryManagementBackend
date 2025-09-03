from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name = "products"),
    path('categories/', views.categories, name = "categories"),
    path('categories/<int:category_id>/', views.category_detail, name = "category_detail"),
    path('sellers/', views.sellers, name="seller"),
    path('transactions/', views.transactions, name="transactions")
    
    
]
