from django.shortcuts import render
from Electrician.models import ElectricianModel
from django.contrib import messages

# Create your views here.
def electrical(request):
    data = ElectricianModel.objects.filter(isactive = 'Yes')
    context = {
        "electricaldata":data
    }
    return render(request,'user/electrical.html',context)

def inquiry(request):
    return render(request,'user/inquiry.html')

def elecdetail(request,id):
    data = ElectricianModel.objects.get(elec_id = id)
    context = {
        "electricaldata":data
    }
    return render(request,'user/inquiry.html',context)

def contact(request):
    return render(request,'user/contact.html')

def article(request):
    return render(request,'user/article.html')

def faq(request):
    return render(request,'user/faq.html')



