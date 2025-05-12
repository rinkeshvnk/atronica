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
    data = ProductsModel.objects.all().values()
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
