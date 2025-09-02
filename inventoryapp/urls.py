from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name = "products"),
    path('category', views.category, name = "category")
    
]
