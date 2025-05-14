from django.shortcuts import render,redirect
from .models import StateModel
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import generics
from .serializers import StateSerializer

class StateListCreateAPIView(generics.ListCreateAPIView):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer

class StateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer
    
# Create your views here.
def addstate(request):
    return render(request,'admin/add_state.html')

def insertstate(request):
    statename = request.POST.get('txtstatename')
    #duplication
    if StateModel.objects.filter(state_name = statename).exists():
         messages.error(request, 'State already exist!')
    else:
        obj = StateModel()
        obj.state_name = statename
        obj.save()

        messages.success(request, 'State Created Successfully!')
    return redirect('/customadmin/state/add')

def viewstate(request):
    data = StateModel.objects.all()
    context = {
        "statedata":data
    }
    return render(request,'admin/view_state.html',context)

def deletestate(request,id):
    StateModel.objects.get(state_id = id).delete()
    messages.success(request, 'State Deleted Successfully!')

    return redirect('/customadmin/state/view')

def editstate(request,id):
    single = StateModel.objects.get(state_id=id)
    context = {
        "data":single
    }
    return render(request,'admin/edit_state.html',context)

def updatestate(request,id):
    statename = request.POST.get('txtstatename')
    obj = StateModel.objects.get(state_id=id)
    obj.state_name = statename
    obj.save()
    messages.success(request, 'State Updated Successfully!')
    return redirect('/customadmin/state/view')

