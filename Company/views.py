from django.shortcuts import render,redirect
from .models import CompanyModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def addcompany(request):
    return render(request,'admin/add_company.html')


def insertCompany(request):
    companyname = request.POST.get("txtcompanyname")
    #duplication
    if CompanyModel.objects.filter(company_name = companyname).exists():
         messages.error(request, 'Company already exist!')
    else:
        #image upload
        companylogo = request.FILES['txtcompanylogo']
        fs = FileSystemStorage()
        file = fs.save(companylogo.name, companylogo)
        imagename = fs.url(file)

        obj = CompanyModel()
        obj.company_name = companyname
        obj.company_logo = imagename
        obj.save()

        messages.success(request, 'Company Created Successfully!')
    return redirect('/customadmin/company/add')

def viewcompany(request):
    data = CompanyModel.objects.all()
    context = {
        "companydata":data
    }
    return render(request,'admin/view_company.html',context)

def editcompany(request,id):
    data = CompanyModel.objects.get(company_id = id)
    context={
        "data":data
    }
    return render(request,'admin/edit_company.html',context)

def updatecompany(request,id):
    obj = CompanyModel.objects.get(company_id = id)
    companyname = request.POST.get("txtcompanyname")
    # Check image selected or not
    if 'txtcompanylogo' in request.FILES:
        company_logo = request.FILES['txtcompanylogo']
        if company_logo:
            # Delete Old Image
            imagepath = obj.company_logo
            if os.path.exists(imagepath):
                os.remove(imagepath)
            # Upload new Image
            companylogo = request.FILES['txtcompanylogo']
            fs = FileSystemStorage()
            file = fs.save(companylogo.name, companylogo)
            imagename = fs.url(file)
        else:
           imagename = obj.company_logo     
    else:
        imagename = obj.company_logo


   
    obj.company_name = companyname
    obj.company_logo = imagename
    obj.save()

    messages.success(request, 'Company Updated Successfully!')
    return redirect('/customadmin/company/view')

def deletecompany(request,id):
    obj = CompanyModel.objects.get(company_id = id)
    imagepath = obj.company_logo
    if os.path.exists(imagepath):
        os.remove(imagepath)
    obj.delete()
    messages.success(request, 'Company Deleted Successfully!')
    return redirect('/customadmin/company/view')