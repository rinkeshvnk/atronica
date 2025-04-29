from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/log/add', views.addlog),
    path('customadmin/log/insert', views.insertlog),
    path('customadmin/log/view', views.viewlog),
    path('customadmin/log/edit/<int:id>', views.editlog),
    path('customadmin/log/update/<int:id>', views.updatelog),
    path('customadmin/log/delete/<int:id>', views.deletelog),
]