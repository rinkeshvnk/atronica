from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/inquries/view', views.viewinquries),
    path('customadmin/inquries/insert', views.insertinquries),
]