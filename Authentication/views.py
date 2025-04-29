from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

# Create your views here.
def addlogin(request):
    return render(request,'admin/login.html')

def checklogin(request):
    uname = request.POST.get("txtusername")
    pwd = request.POST.get("txtpassword")

    user = authenticate (username = uname, password = pwd)

    if user is not None:
        login(request,user)
        return redirect('/customadmin/dashboard')
    else:
        messages.error(request,'Username or password not found')
        return redirect('/customadmin/login')
    
def checklogout(request):
    logout(request)
    return redirect('/customadmin/login')

def changepassword(request):
    return render(request,'admin/change_password.html')

def updatepassword(request):
    oldpass = request.POST.get("txtcurrentpwd")
    newpass = request.POST.get("txtnewpwd")

    user = authenticate (username = request.user.username, password = oldpass)
    if user is not None:
        user.set_password(newpass)
        user.save()
        messages.success(request,'Password Updated Successfully')
        return redirect('/customadmin/changepassword')
    else:
        messages.error(request,'Username or password not found')
        return redirect('/customadmin/changepassword')
   