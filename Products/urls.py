from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/products/add', views.addproducts),
    path('customadmin/products/insert', views.insertproducts),
    path('customadmin/products/edit/<int:id>', views.editproducts),
    path('customadmin/products/view', views.viewproducts),
    path('customadmin/products/delete/<int:id>', views.deleteproducts),
    path('customadmin/products/update/<int:id>', views.updateproducts),
]
