from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import redirect,render
from . models import Categorydb
from . models import Productdb
from UserApp.models import Contactdb
from UserApp.models import Registerb

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    datanew=Registerb.objects.all().count()
    productdata=Productdb.objects.all().count()
    message=Contactdb.objects.all().count()
    return render(request,"admin_index.html",{"datanew":datanew,"productdata":productdata,"message":message})
def form(request):
    return render(request,"categoryform.html")
def formdata(request):
    if request.method=='POST':
        C_name=request.POST['categoryname']
        C_description=request.POST['categorydescription']
        C_image=request.FILES['categoryimage']
        data=Categorydb(Cname=C_name,Cdescription=C_description,Cimage=C_image)
        data.save()
    return redirect('index')
def tabledata(request):
    data=Categorydb.objects.all()
    return render(request,"categorytable.html",{"data":data})
def tabledit(request,tableid):
    data=Categorydb.objects.filter(id=tableid)
    return render(request,"categoryeditable.html",{"data":data})
def updatetable(request,tableid):
    if request.method=='POST':
        cname=request.POST['categoryname']
        cdescription=request.POST['categorydescription']
        try:
            Image = request.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file = Categorydb.objects.get(id=tableid).Cimage
        Categorydb.objects.filter(id=tableid).update(Cname=cname,Cdescription=cdescription,Cimage=file)
    return redirect('tabledata')
def deletion(request,tableid):
     Categorydb.objects.filter(id=tableid).delete()
     return redirect('tabledata')
def adminlogin(request):
    if request.method == 'POST':
        adminusername = request.POST['adminuser']
        adminpassword = request.POST['adminpass']
        user = authenticate(username=adminusername,password=adminpassword)
        if user is not None:
            login(request, user)
            request.session['username_a'] = adminusername
            request.session['password_a'] = adminpassword
            request.session['uid'] = data['id']
            return redirect('index')
        else:
            return render(request,'admin_login.html', {'msg':'Sorry Invalid User Credentials'})
    return render(request,'admin_login.html')
def adminlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    del request.session['uid']
    return redirect('adminlogin')

def viewuser(request):
    data=Registerb.objects.all()
    return render(request,"usersview.html",{"data":data})
    
#Product module
def product(request):
    newdata=Categorydb.objects.all()
    return render(request,"Addproducts.html",{"data1":newdata})
def productadd(request):
    if request.method=='POST':
        prname=request.POST['productname']
        primage=request.FILES['productimage']
        prprice=request.POST['productprize']
        prweight=request.POST['productweight']
        prcategories=request.POST['productcategory']
        data=Productdb(pr_name=prname,pr_image=primage,pr_price=prprice,pr_weight=prweight,categories=prcategories)
        data.save()
    return redirect('index')
def productview(request):
    data=Productdb.objects.all()
    return render(request,"Viewproducts.html",{"data":data})
def productedit(request,productid):
    data=Productdb.objects.filter(id=productid)
    data1=Categorydb.objects.all()
    return render(request,"editproduct.html",{"data":data,"data1":data1})
def productupdate(request,productid):
    if request.method=='POST':
        upname=request.POST['productname']
        upprice=request.POST['productprize']
        upweight=request.POST['productweight']
        upcategory=request.POST['productcategory']
        try:
            upimage = request.FILES['productimage']
            upfs = FileSystemStorage()
            secondfile = upfs.save(upimage.name,upimage)
        except MultiValueDictKeyError:
            secondfile = Productdb.objects.get(id=productid).pr_image
        Productdb.objects.filter(id=productid).update(pr_name=upname,pr_price=upprice,pr_weight=upweight,categories=upcategory,pr_image=secondfile)
    return redirect('productview')
def productdelete(request,productid):
     Productdb.objects.filter(id=productid).delete()
     return redirect('productview')
def messageview(request):
    data=Contactdb.objects.all()
    return render(request,"message.html",{"data":data})
