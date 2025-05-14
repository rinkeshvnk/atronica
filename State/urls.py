from django.contrib import admin
from django.urls import path
from . import views
from .views import StateListCreateAPIView,StateRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('customadmin/state/add', views.addstate),
    path('customadmin/state/insert', views.insertstate),
    path('customadmin/state/view', views.viewstate),
    path('customadmin/state/delete/<int:id>', views.deletestate),
    path('customadmin/state/edit/<int:id>', views.editstate),
    path('customadmin/state/update/<int:id>', views.updatestate),
    path('state/', StateListCreateAPIView.as_view()),
    path('state/<int:pk>/', StateRetrieveUpdateDestroyAPIView.as_view()),
]