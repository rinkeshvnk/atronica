from django.shortcuts import render
from Products.models import ProductsModel
from Company.models import CompanyModel
from Subcategory.models import SubcategoryModel
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def productlist(request):
    data = ProductsModel.objects.filter(isactive = 'Yes')
    catdata = SubcategoryModel.objects.all()
    companydata = CompanyModel.objects.all()
    context = {
        "productdata":data,
        "catdata":catdata,
        "companydata":companydata
    }
    return render(request,'user/shop.html',context)

def productdetail(request,id):
    data = ProductsModel.objects.get(product_id = id)
    realateddata = ProductsModel.objects.all()
    context = {
        "productdata":data,
        "realateddata":realateddata
    }
    return render(request,'user/product_detail.html',context)

def searchproduct(request):
    subcategory = request.POST.getlist("subcategory")
    company = request.POST.getlist("company")
    data = ProductsModel.objects.filter(Q(company_id__in=company) | Q(subcategory_id__in=subcategory))
    catdata = SubcategoryModel.objects.all()
    companydata = CompanyModel.objects.all()
    context = {
        "productdata":data,
        "catdata":catdata,
        "companydata":companydata
    }
    return render(request,'user/shop.html',context)

def searchresult(request):
    q = request.GET.get('q')
    catdata = SubcategoryModel.objects.all()
    companydata = CompanyModel.objects.all()
    data = ProductsModel.objects.filter(title__icontains=q)
    context = {
        "productdata":data,
        "q":q,
        "catdata":catdata,
        "companydata":companydata
    }
    return render(request,'user/searchresult.html',context)

def categoryproduct(request,id):
    data = ProductsModel.objects.filter(isactive = 'Yes',subcategory_id__category_id=id)
    context = {
        "productdata":data,
        
    }
    return render(request,'user/categoryproduct.html',context)