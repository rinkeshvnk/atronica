from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customadmin/login', views.addlogin),
    path('customadmin/checklogin', views.checklogin),
    path('customadmin/checklogout', views.checklogout),
    path('customadmin/changepassword', views.changepassword),
    path('customadmin/updatepassword', views.updatepassword),
]