from django.shortcuts import render,redirect
from .models import CartModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def viewcart(request):
    data = CartModel.objects.all()
    context = {
        "cartdata":data,
    }
    return render(request,'admin/view_cart.html',context)

def deletecart(request,id):
    CartModel.objects.get(cart_id = id).delete()
    messages.success(request,'Cart Deleted Successfully!')

    return redirect('/customadmin/cart/view')