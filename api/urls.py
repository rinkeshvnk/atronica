from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllProducts', views.getAllProducts),
    path('api/insertCategory', views.insertCategory),
    path('api/insertState', views.insertState),
]