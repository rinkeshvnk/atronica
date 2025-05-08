from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Products.models import ProductsModel
# Create your views here.


def getAllProducts(request):
    data = ProductsModel.objects.all().values()
    data = list(data)
    return JsonResponse(data,safe=False)