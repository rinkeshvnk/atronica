from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/user/view', views.viewuser),
    #path('customadmin/user/delete/<int:id>', views.deleteuser),
]