from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/order/view', views.vieworder),
    path('customadmin/order/insert', views.insertorder),
    path('customadmin/order/rpay', views.rpay),
    path('customadmin/order/delete/<int:id>', views.deleteorder),
]