from django.shortcuts import render,redirect
from .models import VariantModel
from Products.models import ProductsModel
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def addvariant(request):
    product = ProductsModel.objects.all()
    context={
        "product":product,
    }
    return render(request,'admin/add_variant.html',context)

def insertvariant(request):
    videourl = request.POST.get('txtvideourl')
    retailprice = request.POST.get('retailprice')
    sellprice = request.POST.get('sellprice')
    description = request.POST.get('txtdescription')
    packaging = request.POST.get('packaging')
    productid = request.POST.get('txtproduct')

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

    obj = VariantModel()
    obj.product_id = ProductsModel.objects.get(product_id  = productid)
    obj.video_url = videourl
    obj.retail_price = retailprice
    obj.sell_price = sellprice
    obj.variant_description = description
    obj.packaging = packaging
    obj.img1 = imagename1
    obj.img2 = imagename2
    obj.img3 = imagename3
    obj.save()

    messages.success(request, 'Variant Created Successfully!')
    return redirect('/customadmin/variant/add')

def viewvariant(request):
    data = VariantModel.objects.all()
    context = {
        "variantdata":data
    }
    return render(request,'admin/view_variant.html',context)

def deletevariant(request,id):
    VariantModel.objects.get(variant_id = id).delete()
    messages.success(request, 'Variant Deleted Successfully!')

    return redirect('/customadmin/variant/view')

def editvariant(request,id):
    product = ProductsModel.objects.all()
    data = VariantModel.objects.get(variant_id = id)
    context={
        "product":product,
        "data":data,
    }
    return render(request,'admin/edit_variant.html',context)

def updatevariant(request,id):
    obj = VariantModel.objects.get(variant_id = id)
    videourl = request.POST.get('txtvideourl')
    retailprice = request.POST.get('retailprice')
    sellprice = request.POST.get('sellprice')
    description = request.POST.get('txtdescription')
    packaging = request.POST.get('packaging')
    productid = request.POST.get('txtproduct')

    #image1
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

    #image2
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

    #image3
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



    obj.product_id = ProductsModel.objects.get(product_id  = productid)
    obj.video_url = videourl
    obj.retail_price = retailprice
    obj.sell_price = sellprice
    obj.variant_description = description
    obj.packaging = packaging
    obj.img1 = imagename1
    obj.img2 = imagename2
    obj.img3 = imagename3
    obj.save()   

    messages.success(request,'Variant Updated Successfully!')
    return redirect('/customadmin/variant/view')

