from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Products.models import ProductsModel
from Category.models import CategoryModel
from State.models import StateModel
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.


def getAllProducts(request):
    data = ProductsModel.objects.filter().values('company_id__company_name','title','sell_price','retail_price','img1','isactive')
    data = list(data)
    return JsonResponse(data,safe=False)

@csrf_exempt
def insertCategory(request):
    category_name = request.POST.get("category_name")
    category_image = request.FILES['category_image']
    
    fs = FileSystemStorage()
    file = fs.save(category_image.name, category_image)
    imagename = fs.url(file)


    obj = CategoryModel()
    obj.category_name = category_name
    obj.category_image = imagename
    obj.save()

    return JsonResponse({"status":True,"message":"Data inserted successfully!"})

@csrf_exempt
def insertState(request):
    state_name = request.POST.get('state_name')

    obj = StateModel()
    obj.state_name = state_name
    obj.save()
    return JsonResponse({"status":True,"message":"Data inserted successfully!"})

@csrf_exempt
def deletecategory(request,id):
    #id = request.POST.get("id")
    CategoryModel.objects.get(category_id = id).delete()
    return JsonResponse({"status":True,"message":"Data Deleted successfully!"})


def getsinglecategory(request,id):
    data = CategoryModel.objects.filter(category_id = id).values().first()
    return JsonResponse(data,safe=False)

@csrf_exempt
def updatecategory(request,id):
    if CategoryModel.objects.filter(category_id = id).exists():
        obj = CategoryModel.objects.get(category_id = id)
        categoryname = request.POST.get("category_name")
        if 'category_image' in request.FILES:
            category_image = request.FILES['category_image']
            if category_image:
                # Delete Old Image
                imagepath = obj.category_image
                if os.path.exists(imagepath):
                    os.remove(imagepath)
                # Upload new Image
                categoryimage = request.FILES['category_image']
                fs = FileSystemStorage()
                file = fs.save(categoryimage.name, categoryimage)
                imagename = fs.url(file)
            else:
                imagename = obj.category_image     
        else:
            imagename = obj.category_image

        obj.category_name = categoryname
        obj.category_image = imagename
        obj.save()
        return JsonResponse({"status":True,"message":"Data Updated successfully!"})
    else:
        return JsonResponse({"status":False,"message":"Error!"})