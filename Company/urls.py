from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/company/add', views.addcompany),
    path('customadmin/company/insert', views.insertCompany),
    path('customadmin/company/view', views.viewcompany),
    path('customadmin/company/delete/<int:id>', views.deletecompany),
    path('customadmin/company/edit/<int:id>', views.editcompany),
    path('customadmin/company/update/<int:id>', views.updatecompany),
]
