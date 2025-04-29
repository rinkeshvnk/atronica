from django.shortcuts import render,redirect
from City.models import CityModel
from .models import ElectricianModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def addelectrician(request):
    city = CityModel.objects.all()
    context={
        "city":city,
    }
    return render(request,'admin/add_electrician.html',context)

def insertelectrician(request):
    mobileno = request.POST.get('txtmobileno')
    name = request.POST.get('txtname')
    experience = request.POST.get('txtexperience')
    aboutelec = request.POST.get('txtaboutelec')
    isactive = request.POST.get('txtactive')
    cityid = request.POST.get('txtcity')
    elecprice = request.POST.get('txtelecprice')

    if ElectricianModel.objects.filter(mobilenumber = mobileno).exists():
        messages.error(request, 'Mobile no already exists')
    else:
        image = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        imagename = fs.url(file)

        obj = ElectricianModel()
        obj.name = name
        obj.img = imagename
        obj.city_id = CityModel.objects.get(city_id = cityid)
        obj.mobilenumber = mobileno
        obj.experience = experience
        obj.aboutelectrician = aboutelec
        obj.elec_price = elecprice
        obj.isactive = isactive
        obj.save()

        messages.error(request, 'Mobile no already exists')
    return redirect('/customadmin/electrician/add')

def viewelectrician(request):
    data = ElectricianModel.objects.all()
    context = {
        "elecdata":data
    }
    return render(request,'admin/view_electrician.html',context)

def editelectrician(request,id):
    city = CityModel.objects.all()
    data = ElectricianModel.objects.get(elec_id = id)
    context={
        "city":city,
        "data":data
    }
    return render(request,'admin/edit_electrician.html',context)

def updateelectrician(request,id):
    obj = ElectricianModel.objects.get(elec_id = id)
    name = request.POST.get('txtname')
    mobileno = request.POST.get('txtmobileno')
    experience = request.POST.get('txtexperience')
    aboutelec = request.POST.get('txtaboutelec')
    isactive = request.POST.get('txtactive')
    cityid = request.POST.get('txtcity')
    elecprice = request.POST.get('txtelecprice')

    # Check image selected or not
    if 'image' in request.FILES:
        img = request.FILES['image']
        if img:
            # Delete Old Image
            imagepath = obj.img
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
            imagename = fs.url(file)
        else:
           imagename = obj.img     
    else:
        imagename = obj.img

    obj.name = name
    obj.city_id = CityModel.objects.get(city_id = cityid)
    obj.img = imagename
    obj.mobilenumber = mobileno
    obj.experience = experience
    obj.aboutelectrician = aboutelec
    obj.elec_price = elecprice
    obj.isactive = isactive
    obj.save()
    return redirect('/customadmin/electrician/view')

def deleteelectrician(request,id):
    obj = ElectricianModel.objects.get(elec_id = id)
    imagepath = obj.img
    if os.path.exists(imagepath):
        os.remove(imagepath)
    obj.delete()
    return redirect('/customadmin/electrician/view')