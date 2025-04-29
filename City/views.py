from django.shortcuts import render,redirect
from .models import CityModel
from State.models import StateModel
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def addcity(request):
    state = StateModel.objects.all()
    context={
        "state":state,
    }
    return render(request,'admin/add_city.html',context)

def insertcity(request):
    cityname = request.POST.get('txtcityname')
    stateid = request.POST.get('txtstate')
    #duplication
    if CityModel.objects.filter(city_name = cityname).exists():
         messages.error(request, 'City already exist!')
    else:
        obj = CityModel()
        obj.state_id = StateModel.objects.get(state_id = stateid)
        obj.city_name = cityname
        obj.save()

        messages.success(request, 'City Created Successfully!')
    return redirect('/customadmin/city/add')

def viewcity(request):
    data = CityModel.objects.all()
    context = {
        "citydata":data
    }
    return render(request,'admin/view_city.html',context)

def deletecity(request,id):
    CityModel.objects.get(city_id = id).delete()
    messages.success(request, 'City Deleted Successfully!')

    return redirect('/customadmin/city/view')

def editcity(request,id):
    state = StateModel.objects.all()
    data = CityModel.objects.get(city_id = id)
    context={
        "state":state,
        "data":data
    }
    return render(request,'admin/edit_city.html',context)


def updatecity(request,id):
    cityname = request.POST.get('txtcityname')
    stateid = request.POST.get('txtstate')

    obj = CityModel.objects.get(city_id = id)
    obj.state_id = StateModel.objects.get(state_id = stateid)
    obj.city_name = cityname
    obj.save()

    messages.success(request, 'City Updated Successfully!')
    return redirect('/customadmin/city/view')