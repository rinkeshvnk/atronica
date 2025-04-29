from django.shortcuts import render,redirect
from .models import PincodeModel
from django.contrib import messages
# Create your views here.
def addpincode(request):
    return render(request,'admin/add_pincode.html')

def insertpincode(request):
    pincode = request.POST.get('txtpincode')

    if PincodeModel.objects.filter(pincode = pincode).exists():
         messages.error(request, 'Pincode already exist!')
    else:    
        obj = PincodeModel()
        obj.pincode = pincode
        obj.save()

    return redirect('/customadmin/pincode/add')

def checkpincode(request,id):
    pincode  = request.POST.get("txtpincode")
    data = PincodeModel.objects.filter(pincode = pincode)
    if len(data) <=0:
        messages.error(request, 'Delivery not available')
    else:
        messages.success(request, 'Delivery available!')
    return redirect("/productdetail/"+str(id))

def viewpincode(request):
    data = PincodeModel.objects.all()
    context = {
        "pincodedata":data
    }
    return render(request,'admin/view_pincode.html',context)

def deletepincode(request,id):
    PincodeModel.objects.get(pincode_id = id).delete()
    messages.success(request, 'Pincode Deleted Successfully!')

    return redirect('/customadmin/pincode/view')
    