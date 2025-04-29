from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/variant/add', views.addvariant),
    path('customadmin/variant/view', views.viewvariant),
    path('customadmin/variant/insert', views.insertvariant),
    path('customadmin/variant/delete/<int:id>', views.deletevariant),
    path('customadmin/variant/edit/<int:id>', views.editvariant),
    path('customadmin/variant/update/<int:id>', views.updatevariant),
]