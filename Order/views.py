from django.shortcuts import render,redirect
from .models import OrderModel
from django.contrib import messages
from City.models import CityModel
from Item.models import ItemModel
from Cart.models import CartModel
from Products.models import ProductsModel
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
def rpay(request):
    totalpay = request.POST.get('txttotalpayment')
    order_amount = float(totalpay) * 100
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'

    razorpay_order = client.order.create(dict(
        amount=order_amount,
        currency=order_currency,
        receipt=order_receipt,
        payment_capture='1'
    ))
    cityid = request.POST.get('txtcity')
    totalpay = request.POST.get('txttotalpayment')
    add1 = request.POST.get('txtaddress1')
    add2 = request.POST.get('txtaddress2')
    pincode = request.POST.get('txtpincode')
    delvcharge = request.POST.get('txtdeliverycharge')
    paytype = request.POST.get('txtpaytype')
    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
        'amount': order_amount,
        'currency': order_currency,
        'cityid':cityid,
        'totalpay':totalpay,
        'add1':add1,
        'add2':add2,
        'pincode':pincode,
        'delvcharge':delvcharge,
        'paytype':paytype,
        'userid':request.user.id
    }
    return render(request, 'user/payment.html', context)

@csrf_exempt
def insertorder(request):
    data = request.POST
    cityid = request.POST.get('cityid')
    totalpay = request.POST.get('totalpay')
    add1 = request.POST.get('add1')
    add2 = request.POST.get('add2')
    pincode = request.POST.get('pincode')
    delvcharge = request.POST.get('delvcharge')
    paytype = 'online'
    userid = request.POST.get('userid')
    
    obj = OrderModel()
    obj.city_id = CityModel.objects.get(city_id = cityid)
    obj.total_payment = totalpay
    obj.address1 = add1
    obj.address2 = add2
    obj.pincode = pincode
    obj.user_id = User.objects.get(id = userid)
    obj.deliverycharge = delvcharge
    obj.paytype = paytype
    obj.transaction_number = data.get('razorpay_payment_id')
    obj.status = "pending"
    obj.save()

    oid = obj.order_id

    cartdata = CartModel.objects.filter(user_id = userid)
    for row in cartdata:
        itemobj = ItemModel()
        itemobj.order_id = OrderModel.objects.get(order_id = oid)
        itemobj.product_id = row.product_id
        itemobj.price = row.price
        itemobj.qty = row.qty
        itemobj.save()
        row.delete()
    return redirect('/')


def vieworder(request):
    data = OrderModel.objects.all()
    context = {
        "orderdata":data
    }
    return render(request,'admin/view_order.html',context)

def deleteorder(request,id):
    OrderModel.objects.get(order_id = id).delete()
    messages.success(request, 'Order Deleted Successfully!')

    return redirect('/customadmin/order/view')

