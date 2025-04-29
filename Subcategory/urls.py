from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/subcategory/add', views.addsubcategory),
    path('customadmin/subcategory/view', views.viewsubcategory),
    path('customadmin/subcategory/insert', views.insertsubcategory),
    path('customadmin/subcategory/delete/<int:id>', views.deletesubcategory),
    path('customadmin/subcategory/edit/<int:id>', views.editsubcategory),
    path('customadmin/subcategory/update/<int:id>', views.updatesubcategory),
]
