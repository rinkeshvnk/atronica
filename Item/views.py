from django.shortcuts import render,redirect
from .models import ItemModel
from Log.models import LogModel
from django.contrib import messages

# Create your views here.
def viewitem(request,orderid):
    data = ItemModel.objects.filter(order_id = orderid)
    logdata = LogModel.objects.filter(order_id = orderid)
    context = {
        "itemdata":data,
        "logdata":logdata
    }
    return render(request,'admin/view_item.html',context)

def deleteitem(request,id):
    ItemModel.objects.get(item_id = id).delete()
    messages.success(request,'Item Deleted Successfully!')

    return redirect('/customadmin/item/view')


