from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart),
    path('addtocart', views.addtocart),
    path('checkout', views.checkout),
    path('wishlist', views.wishlist),
    path('cart/delete/<int:id>', views.deletecart),
    path('myitem/<int:id>', views.myitem),
    path('myorder', views.myorder),
    path('loadajaxcart', views.loadajaxcart),
    path('myprofile', views.myprofile),
    path('changestatus/<int:id>', views.changestatus),
]