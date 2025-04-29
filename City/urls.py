from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/city/add', views.addcity),
    path('customadmin/city/insert', views.insertcity),
    path('customadmin/city/view', views.viewcity),
    path('customadmin/city/delete/<int:id>', views.deletecity),
    path('customadmin/city/edit/<int:id>', views.editcity),
    path('customadmin/city/update/<int:id>', views.updatecity),
]