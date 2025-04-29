"""
URL configuration for atronica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashboard.urls')),
    path('', include('Category.urls')),
    path('', include('Subcategory.urls')),
    path('', include('Company.urls')),
    path('', include('Products.urls')),
    path('', include('Variant.urls')),
    path('', include('User.urls')),
    path('', include('Cart.urls')),
    path('', include('Order.urls')),
    path('', include('Item.urls')),
    path('', include('Log.urls')),
    path('', include('State.urls')),
    path('', include('City.urls')),
    path('', include('Electrician.urls')),
    path('', include('Inquries.urls')),
    path('', include('Authentication.urls')),
    path('', include('Home.urls')),
    path('', include('Userproduct.urls')),
    path('', include('Usercart.urls')),
    path('', include('Userauth.urls')),
    path('', include('Userelect.urls')),
    path('', include('Search.urls')),
    path('', include('Pincode.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)