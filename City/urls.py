from django.contrib import admin
from django.urls import path
from . import views
from .views import CityListCreateAPIView,CityRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('customadmin/city/add', views.addcity),
    path('customadmin/city/insert', views.insertcity),
    path('customadmin/city/view', views.viewcity),
    path('customadmin/city/delete/<int:id>', views.deletecity),
    path('customadmin/city/edit/<int:id>', views.editcity),
    path('customadmin/city/update/<int:id>', views.updatecity),
    path('city/', CityListCreateAPIView.as_view()),
    path('city/<int:pk>/', CityRetrieveUpdateDestroyAPIView.as_view())
]