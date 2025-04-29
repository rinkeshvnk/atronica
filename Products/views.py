from django.shortcuts import render,redirect
from .models import ProductsModel
from Subcategory.models import SubcategoryModel
from Company.models import CompanyModel
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def addproducts(request):
    subcat = SubcategoryModel.objects.all()
    company = CompanyModel.objects.all()
    context={
        "subcat":subcat,
        "company":company
    }
    return render(request,'admin/add_products.html',context)

def insertproducts(request):
    title = request.POST.get('txtproductstitle')
    specification = request.POST.get('txtspecification')
    description = request.POST.get('txtdescription')
    retailprice = request.POST.get('txtretailprice')
    sellprice = request.POST.get('txtsellprice')
    videourl = request.POST.get('txtvideourl')
    type = request.POST.get('txttype')
    packaging = request.POST.get('txtpackaging')
    isactive = request.POST.get('txtactive')

    subcatid = request.POST.get('txtsubcat')
    companyid = request.POST.get('txtcompany')

    image1 = request.FILES['image1']
    fs = FileSystemStorage()
    file = fs.save(image1.name, image1)
    imagename1 = fs.url(file)

    image2 = request.FILES['image2']
    fs = FileSystemStorage()
    file = fs.save(image2.name, image2)
    imagename2 = fs.url(file)

    image3 = request.FILES['image3']
    fs = FileSystemStorage()
    file = fs.save(image3.name, image3)
    imagename3 = fs.url(file)



    obj = ProductsModel()
    obj.subcategory_id = SubcategoryModel.objects.get(subcategory_id  = subcatid)
    obj.company_id = CompanyModel.objects.get(company_id = companyid)
    obj.title = title
    obj.specification = specification
    obj.description = description
    obj.retail_price = retailprice
    obj.sell_price = sellprice
    obj.img1 = imagename1
    obj.img2 = imagename2
    obj.img3 = imagename3
    obj.video_url = videourl
    obj.type = type
    obj.packaging = packaging
    obj.isactive = isactive
    obj.save()

    return redirect('/customadmin/products/add')

def viewproducts(request):
    data = ProductsModel.objects.all()
    context = {
        "productdata":data,
    }

    
    return render(request,'admin/view_products.html',context)

def deleteproducts(request,id):
    obj = ProductsModel.objects.get(product_id = id)
    
    imagepath = obj.img1
    if os.path.exists(imagepath):
        os.remove(imagepath)
    obj.delete()
    
    imagepath = obj.img2
    if os.path.exists(imagepath):
        os.remove(imagepath)
    obj.delete()

    imagepath = obj.img3
    if os.path.exists(imagepath):
        os.remove(imagepath)
    ProductsModel.objects.get(product_id = id).delete()
    
    messages.success(request, 'Product Deleted Successfully!')
    return redirect('/customadmin/products/view')

def editproducts(request,id):
    subcat = SubcategoryModel.objects.all()
    company = CompanyModel.objects.all()
    data = ProductsModel.objects.get(product_id = id)
    context={
        "subcat":subcat,
        "company":company,
        "data":data,
    }
    return render(request,'admin/edit_products.html',context)

def updateproducts(request,id):
    obj = ProductsModel.objects.get(product_id = id)
    title = request.POST.get('txtproductstitle')
    specification = request.POST.get('txtspecification')
    description = request.POST.get('txtdescription')
    retailprice = request.POST.get('txtretailprice')
    sellprice = request.POST.get('txtsellprice')
    videourl = request.POST.get('txtvideourl')
    type = request.POST.get('txttype')
    packaging = request.POST.get('txtpackaging')
    isactive = request.POST.get('txtactive')
    subcatid = request.POST.get('txtsubcat')
    companyid = request.POST.get('txtcompany')

    #img1
    if 'image1' in request.FILES:
        image1 = request.FILES['image1']
        if image1:
            # Delete Old Image
            imagepath = obj.img1
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            image1 = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(image1.name, image1)
            imagename1 = fs.url(file)
        else:
            imagename1 = obj.img1     
    else:
        imagename1 = obj.img1

    #img2
    if 'image2' in request.FILES:
        image2 = request.FILES['image2']
        if image2:
            # Delete Old Image
            imagepath = obj.img2
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            image2 = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(image2.name, image2)
            imagename2 = fs.url(file)
        else:
            imagename2 = obj.img2     
    else:
        imagename2 = obj.img2

    #img3
    if 'image3' in request.FILES:
        image3 = request.FILES['image3']
        if image3:
            # Delete Old Image
            imagepath = obj.img3
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            image3 = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(image3.name, image3)
            imagename3 = fs.url(file)
        else:
            imagename3 = obj.img3     
    else:
        imagename3 = obj.img3



    obj.subcategory_id = SubcategoryModel.objects.get(subcategory_id  = subcatid)
    obj.company_id = CompanyModel.objects.get(company_id = companyid)
    obj.title = title
    obj.specification = specification
    obj.description = description
    obj.retail_price = retailprice
    obj.sell_price = sellprice
    obj.img1 = imagename1
    obj.img2 = imagename2
    obj.img3 = imagename3
    obj.video_url = videourl
    obj.type = type
    obj.packaging = packaging
    obj.isactive = isactive
    obj.save()

    return redirect('/customadmin/products/view')