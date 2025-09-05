from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name = "products"),
    path('addproduct/', views.add_product, name = "add_product"),
    path('product/<int:product_id>/edit', views.product_edit, name ="product_edit"),
    path('product/<int:product_id>/delete', views.product_delete, name ="product_delete"),
    path('categories/', views.categories, name = "categories"),
    path('addcategory/', views.add_category, name = "add_category"),
    path('categories/<int:category_id>/', views.category_detail, name = "category_detail"),
    path('categories/<int:category_id>/edit/', views.category_edit, name ="category_edit"),
    path('categories/<int:category_id>/delete/',views.category_delete, name="category_delete"),
    path('sellers/', views.sellers, name="sellers"),
    path('transactions/', views.transactions_view, name="transactions_view"),
    path("transactions/sell", views.sell, name="sell"),
    path("transactions/return", views.sell_return, name="sell_return")
    
    
]
