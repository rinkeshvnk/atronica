from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.
def clogin(request):
    return render(request,'user/login.html')

def checkuserlogin(request):
    loginemail = request.POST.get("txtloginemail")
    loginpassword = request.POST.get("txtloginpassword")

    user = authenticate(username = loginemail, password = loginpassword)

    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        messages.error(request,'Email or password not found')
        return redirect('/login')
    
def userlogout(request):
    logout(request)
    return redirect("/login")


def register(request):
    return render(request,'user/register.html')


def registeruser(request):
    firstname = request.POST.get("txtfirstname")
    lastname = request.POST.get("txtlastname")
    email = request.POST.get("txtemail")
    phone = request.POST.get("txtphone")
    password = request.POST.get("txtpassword")

    if User.objects.filter(email = email).exists():
        messages.error(request, 'Email id already registered!')
        return redirect('/register')
    else:
        user = User.objects.create_user(email,email, password)
        user.first_name= firstname
        user.last_name = lastname
        user.save()
        messages.success(request, 'Register Successfully!')
        return redirect("/login")


def changepassword(request):
    return render(request,'user/changepassword.html')

def updatepassword(request):
    oldpass = request.POST.get("txtcurrpassword")
    newpass = request.POST.get("txtnewpassword")

    user = authenticate (username = request.user.username, password = oldpass)
    if user is not None:
        user.set_password(newpass)
        user.save()
        messages.success(request,'Password Updated Successfully')
        return redirect("/login")
    else:
        messages.error(request,'Username or password not found')
        return redirect("/login")

def forgetpassword(request):
    return render (request,'user/forgetpassword.html')
