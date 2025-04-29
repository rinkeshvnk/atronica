from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/item/view/<int:orderid>', views.viewitem),
    path('customadmin/item/delete/<int:id>', views.deleteitem),
]