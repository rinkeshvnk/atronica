from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('electrical', views.electrical),
    path('inquiry', views.inquiry),
    path('elecdetail/<int:id>', views.elecdetail),
    path('contact', views.contact),
    path('article', views.article),
    path('faq', views.faq),
]