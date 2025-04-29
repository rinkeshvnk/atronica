from django.shortcuts import render,redirect
from .models import CategoryModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def addcategory(request):
    return render(request,'admin/add_category.html')

def insertcategory(request):
    categoryname = request.POST.get("txtcategoryname")
    #duplication
    if CategoryModel.objects.filter(category_name = categoryname).exists():
        messages.error(request, 'Category already exists')
    else:
        #image upload
        categoryimage = request.FILES['txtcategoryimage']
        fs = FileSystemStorage()
        file = fs.save(categoryimage.name, categoryimage)
        imagename = fs.url(file)


        obj = CategoryModel()
        obj.category_name = categoryname
        obj.category_image = imagename
        obj.save()

        messages.success(request, 'Category Added Successfully!')
    return redirect('/customadmin/category/add')

def viewcategory(request):
    data = CategoryModel.objects.all()
    context = {
        "categorydata":data
    }

    return render(request,'admin/view_category.html',context)

def editcategory(request,id):
    data = CategoryModel.objects.get(category_id = id)
    context={
        "data":data
    }
    return render(request,'admin/edit_category.html',context)

def updatecategory(request,id):
    obj = CategoryModel.objects.get(category_id = id)
    categoryname = request.POST.get("txtcategoryname")

    # Check image selected or not
    if 'txtcategoryimage' in request.FILES:
        category_image = request.FILES['txtcategoryimage']
        if category_image:
            # Delete Old Image
            imagepath = obj.category_image
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            categoryimage = request.FILES['txtcategoryimage']
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

    messages.success(request, 'Category Updated Successfully!')
    return redirect('/customadmin/category/view')

def deletecategory(request,id):
    obj = CategoryModel.objects.get(category_id = id)
    imagepath = obj.category_image
    if os.path.exists(imagepath):
        os.remove(imagepath)
    obj.delete()
    messages.success(request, 'Category Deleted Successfully!')
    return redirect('/customadmin/category/view')