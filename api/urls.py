from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllProducts', views.getAllProducts),
    path('api/insertCategory', views.insertCategory),
    path('api/insertState', views.insertState),
    path('api/deletecategory/<int:id>', views.deletecategory),
    path('api/getsinglecategory/<int:id>', views.getsinglecategory),
    path('api/updatecategory/<int:id>', views.updatecategory),
]