from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/electrician/add', views.addelectrician),
    path('customadmin/electrician/insert', views.insertelectrician),
    path('customadmin/electrician/view', views.viewelectrician),
    path('customadmin/electrician/edit/<int:id>', views.editelectrician),
    path('customadmin/electrician/update/<int:id>', views.updateelectrician),
    path('customadmin/electrician/delete/<int:id>', views.deleteelectrician),
]