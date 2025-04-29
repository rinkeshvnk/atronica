from django.shortcuts import render
from Products.models import ProductsModel
from django.contrib.auth.models import User

# Create your views here.

def search(request):
    q = request.GET.get('search')
    data = ProductsModel.objects.filter(title__icontains = q)
    auth = User.objects.filter(is_superuser=0,first_name__icontains = q)
    context = {
        "productdata":data,
        "authuser":auth,
    }
    return render(request,'admin/search.html',context)
