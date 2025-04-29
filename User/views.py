from django.shortcuts import render,redirect
from .models import UserModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def viewuser(request):
    data = User.objects.filter(is_superuser = 0)
    context = {
        "userdata":data
    }
    return render(request,'admin/view_user.html',context)

#def deleteuser(request,id):
    UserModel.objects.get(user_id = id).delete()
    messages.success(request, 'User Deleted Successfully!')

    return redirect('/customadmin/city/view')
    

