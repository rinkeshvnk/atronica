from django.shortcuts import render,redirect
from .models import InquriesModel
from Electrician.models import ElectricianModel

# Create your views here.
def viewinquries(request):
    data = InquriesModel.objects.all()
    context = {
        "inquriesdata":data
    }
    return render(request,'admin/view_inquries.html',context)

def insertinquries(request):
    txtid = request.POST.get('txtid')
    name = request.POST.get('txtname')
    mobileno = request.POST.get('txtmobileno')
    message = request.POST.get('txtmessage')

    obj = InquriesModel()
    obj.name = name
    obj.mobile_num = mobileno
    obj.message = message
    obj.elec_id = ElectricianModel.objects.get(elec_id = txtid)
    obj.save()
    
    return redirect ('/')