from django.shortcuts import render
from Electrician.models import ElectricianModel
from Products.models import ProductsModel

# Create your views here.
def loadhome(request):
    data = ElectricianModel.objects.all()
    product = ProductsModel.objects.all()
    productcat8 = ProductsModel.objects.filter(subcategory_id = 6)[:3]
    productcat9 = ProductsModel.objects.filter(subcategory_id = 12)[:3]
    productcat10 = ProductsModel.objects.filter(subcategory_id = 10)[:3]
    context = {
        "electricaldata":data,
        "productdata":product,
        "productcat8":productcat8,
        "productcat9":productcat9,
        "productcat10":productcat10,
    }
    return render(request,'user/home.html',context)

def loadabout(request):
    return render(request,'user/about.html')