from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.productlist),
    path('searchproduct', views.searchproduct),
    path('productdetail/<int:id>', views.productdetail),
    path('searchresult', views.searchresult),
    path('categoryproduct/<int:id>', views.categoryproduct),
]