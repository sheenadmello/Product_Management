from django.urls import path

from . import views



urlpatterns = [

  path('products/', views.product_list, name='product-list'),

  path('products/create/', views.product_create, name='product-create'),

  path('products/<int:pk>/', views.product_detail, name='product-detail'),

]