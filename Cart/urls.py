from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/cart/view', views.viewcart),
    path('customadmin/cart/delete/<int:id>', views.deletecart),
]