from django.shortcuts import render,redirect
from Cart.models import CartModel
from Products.models import ProductsModel
from django.contrib import messages
from django.contrib.auth.models import User
from Order.models import OrderModel
from City.models import CityModel
from Item.models import ItemModel
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def cart(request):
    cartdata = CartModel.objects.filter(user_id = request.user.id)
    finaltotal=0
    data =[]
    for row in cartdata:
        data.append({
            "image":row.product_id.img1,
            "title":row.product_id.title,
            "qty":row.qty,
            "price":row.price,
            "cart_id":row.cart_id,
            "total":float(row.price) * int(row.qty),
        })
        finaltotal = finaltotal + (int(row.qty) * float(row.price))

    
    
    context = {
        "cartdata":data,
        "finaltotal":finaltotal,
        
    }
    return render(request,'user/cart.html',context)

  

def checkout(request):
    cartdata = CartModel.objects.filter(user_id = request.user.id)
    finaltotal=0
    data =[]
    for row in cartdata:
        data.append({
            "image":row.product_id.img1,
            "title":row.product_id.title,
            "qty":row.qty,
            "price":row.price,
            "total":float(row.price) * int(row.qty),
        })
        finaltotal = finaltotal + (int(row.qty) * float(row.price))

    
    city = CityModel.objects.all()
    context = {
        "cartdata":data,
        "finaltotal":finaltotal,
        "city":city,
    }
    return render(request,'user/checkout.html',context)

def wishlist(request):
    return render(request,'user/wishlist.html')

def addtocart(request):
    qty = request.POST.get("qty")
    price = request.POST.get("price")
    pid = request.POST.get("pid")
    
    if CartModel.objects.filter(product_id = pid).filter(user_id =  request.user.id).exists():
        obj = CartModel.objects.filter(user_id =  request.user.id).get(product_id = pid)
        qty = int(qty) + int(obj.qty)
    else:
        obj = CartModel()
    obj.qty = qty
    obj.price = price
    obj.product_id = ProductsModel.objects.get(product_id = pid)
    obj.user_id = User.objects.get(id = request.user.id)
    obj.save()

    messages.success(request, 'Product Added Successfully!')
    return redirect('/productdetail/'+pid)

def deletecart(request,id):
    CartModel.objects.get(cart_id = id).delete()
    

    messages.success(request, 'Cart Deleted Successfully!')
    return redirect('/cart')

def myitem(request,id):
    data = ItemModel.objects.filter(order_id = id)
    context = {
        "itemdata":data,
        "id":id
    }
    
    return render(request,'user/myitem.html',context)


def myorder(request):
    data = OrderModel.objects.filter(user_id = request.user.id)
    context = {
        "orderdata":data
    }
    
    return render(request,'user/myorder.html',context)


@csrf_exempt
def loadajaxcart(request):
    cartdata = CartModel.objects.filter(user_id = request.user.id)
    finaltotal=0
    data =[]
    for row in cartdata:
        data.append({
            "image":row.product_id.img1,
            "title":row.product_id.title,
            "qty":row.qty,
            "price":row.price,
            "total":float(row.price) * int(row.qty),
        })
        finaltotal = finaltotal + (int(row.qty) * float(row.price))
    context = {
        "cartdata":data,
        "finaltotal":finaltotal,
        "cartcount":len(cartdata)
    }
    return JsonResponse(context)

def myprofile(request):
    if request.method == "POST":
        fname = request.POST.get("txtfirstname")
        lname = request.POST.get("txtlname")
        email = request.POST.get("txtemail")

        obj = User.objects.get(id = request.user.id)
        obj.first_name = fname
        obj.last_name = lname
        obj.email = email
        obj.save()
        return redirect("/")
    else:
        return render(request,'user/myprofile.html')
    
def changestatus(request,id):
    obj = OrderModel.objects.get(order_id = id)
    obj.status = "cancel"
    obj.save()

    return redirect("/myorder")