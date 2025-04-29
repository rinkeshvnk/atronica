from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/pincode/add', views.addpincode),
    path('customadmin/pincode/insert', views.insertpincode),
    path('customadmin/pincode/view', views.viewpincode),
    path('customadmin/pincode/delete/<int:id>', views.deletepincode),
    path('checkpincode/<int:id>', views.checkpincode),
]