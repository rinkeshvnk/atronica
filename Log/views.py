from django.shortcuts import render,redirect
from .models import LogModel
from Order.models import OrderModel
from django.contrib import messages

# Create your views here.
def addlog(request):
    order = OrderModel.objects.all()
    context={
        "order":order,
    }
    return render(request,'admin/add_log.html',context)

def insertlog(request):
    orderid = request.POST.get('txtorder')
    status = request.POST.get('txtstatus')

    obj = LogModel()
    obj.order_id = OrderModel.objects.get(order_id = orderid)
    obj.status = status
    obj.save()


    orderobj = OrderModel.objects.get(order_id = orderid)
    orderobj.status=status
    orderobj.save()

    return redirect('/customadmin/log/add')

def viewlog(request):
    data = LogModel.objects.all()
    context = {
        "logdata":data
    }
    return render(request,'admin/view_log.html',context)

def editlog(request,id):
    order = OrderModel.objects.all()
    data = LogModel.objects.get(log_id = id)
    context={
        "order":order,
        "data":data,
    }
    return render(request,'admin/edit_log.html',context)

def updatelog(request,id):
    obj = LogModel.objects.get(log_id = id)
    orderid = request.POST.get('txtorder')
    status = request.POST.get('txtstatus')

    obj.order_id = OrderModel.objects.get(order_id = orderid)
    obj.status = status
    obj.save()

    messages.success(request,'Log Updated Successfully!')
    return redirect('/customadmin/log/view')


def deletelog(request,id):
    LogModel.objects.get(log_id = id).delete()

    messages.success(request,'Log Deleted Successfully!')
    return redirect ('/customadmin/log/view')
