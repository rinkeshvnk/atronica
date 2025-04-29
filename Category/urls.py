from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/category/add', views.addcategory),
    path('customadmin/category/insert', views.insertcategory),
    path('customadmin/category/view', views.viewcategory),
    path('customadmin/category/edit/<int:id>', views.editcategory),
    path('customadmin/category/update/<int:id>', views.updatecategory),
    path('customadmin/category/delete/<int:id>', views.deletecategory),
]
