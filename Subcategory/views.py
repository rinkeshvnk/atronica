from django.shortcuts import render,redirect
from Category.models import CategoryModel
from .models import SubcategoryModel
from django.contrib import messages
# Create your views here.
def addsubcategory(request):
    data = CategoryModel.objects.all()
    context={
        "categorydata":data
    }
    return render(request,'admin/add_subcategory.html',context)

def viewsubcategory(request):
    data = SubcategoryModel.objects.all()
    context = {
        "subcategorydata":data
    }
    return render(request,'admin/view_subcategory.html',context)

def insertsubcategory(request):
    catid = request.POST.get("txtcat")
    subcatname = request.POST.get("txtsubcatname")

    obj = SubcategoryModel()
    obj.subcategory_name = subcatname
    obj.category_id = CategoryModel.objects.get(category_id = catid)
    obj.save()

    messages.success(request, 'Subcategory Added Successfully!')
    return redirect('/customadmin/subcategory/add')

def deletesubcategory(request,id):
    SubcategoryModel.objects.get(subcategory_id = id).delete()
    messages.success(request, 'Subcategory Deleted Successfully!')

    return redirect('/customadmin/subcategory/view')

def editsubcategory(request,id):
    cate = CategoryModel.objects.all()
    data = SubcategoryModel.objects.get(subcategory_id = id)
    context={
        "categorydata":cate,
        "data":data,
    }
    return render(request,'admin/edit_subcategory.html',context)

def updatesubcategory(request,id):
    catid = request.POST.get("txtcat")
    subcatname = request.POST.get("txtsubcatname")

    obj = SubcategoryModel(subcategory_id = id)
    obj.subcategory_name = subcatname
    obj.category_id = CategoryModel.objects.get(category_id = catid)
    obj.save()
    return redirect('/customadmin/subcategory/view')