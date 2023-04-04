from django.shortcuts import render,redirect
from dailymartapp.models import Categorydb
from dailymartapp.models import Productdb
from django.db.models import Sum
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Contactdb
from .models import Registerb
from .models import Cart
from .models import Checkout

# Create your views here.
def userindex(request):
    data=Categorydb.objects.all()
    secondata=Productdb.objects.filter()
    cartcount=Cart.objects.all().count()
    return render(request,"userindex.html",{"data":data,"prdata":secondata,"cartcount":cartcount})

def useregister(request):
    return render(request,"useregister.html")

def registerpage(request):
     if request.method=="POST":
        u_username=request.POST.get('user')
        u_password=request.POST.get('pass')
        u_phonenum=request.POST['phone']
        data=Registerb(username=u_username,password=u_password,phonenum=u_phonenum)
        data.save()
        return redirect('ulogin')

def ulogin(request):
    return render(request,"userlogin.html")

def userlogin(request):
    if request.method == "POST":
        uusername = request.POST.get('user')
        upassword = request.POST.get('pass')
        if Registerb.objects.filter(username=uusername,password=upassword).exists():
            data = Registerb.objects.filter(username=uusername,password=upassword).values('phonenum','id').first()
            request.session['nphone'] = data['phonenum']
            request.session['nusername'] = uusername
            request.session['npassword'] = upassword
            request.session['uid'] = data['id']
            return redirect('userindex')
        else:
            return render(request,'userlogin.html',{'msg':'invalid user credentials'})

def usershop(request,cat):
    data=Categorydb.objects.filter()
    cartcount=Cart.objects.all().count()
    if(cat=="all"):
        prdata=Productdb.objects.all()
    else:
        prdata=Productdb.objects.filter(categories=cat)
    return render(request,"shop.html",{"data":data,"prdata":prdata,"cartcount":cartcount})

def userabout(request):
    return render(request,"about.html")

def usercart(request):
    userid=request.session.get('uid')
    data=Cart.objects.filter(userid=userid,status=0)
    cartcount=Cart.objects.all().count()
    return render(request,"cart.html",{"data":data,"cartcount":cartcount})

def usercheckout(request):
    userid=request.session.get('uid')
    newdata=Cart.objects.filter(userid=userid,status=0)
    cartcount=Cart.objects.all().count()
    utotal=Cart.objects.filter(userid=userid,status=0).aggregate(Sum('total'))
    return render(request,"checkout.html",{"data":newdata,"total":utotal,"cartcount":cartcount})

def checkout(request):
    if request.method=='POST':
        f_name=request.POST['firstname']
        l_name=request.POST['lastname']
        c_country=request.POST['chcountry']
        s_address=request.POST['chaddress']
        p_code=request.POST['pin']
        c_city=request.POST['town']
        c_email=request.POST['chemail']
        c_phone=request.POST['chphone']
        user=request.session.get('uid')
        obj=Cart.objects.filter(userid=user,status=1)
        for i in obj:
            cart=Cart.objects.get(id=i.id)
            data=Checkout(userid=user,cartid=cart,fname=f_name,lname=l_name,country=c_country,saddress=s_address,pcode=p_code,city=c_city,cemail=c_email,cphone=c_phone)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('userindex')

@csrf_exempt
def cartupdate(request):
    if request.method=="POST":
        cartid=request.POST.get('cid')
        qt=request.POST.get('qtny')
        pr=request.POST.get('prize')
        grandtotal=float(qt)*float(pr)
        Cart.objects.filter(id=cartid).update(total=grandtotal,quantity=qt)
        return HttpResponse()


def usercontact(request):
    cartcount=Cart.objects.all().count()
    return render(request,"contact.html",{"cartcount":cartcount})

def contactdata(request):
    if request.method=="POST":
        coname=request.POST['contactname']
        coemail=request.POST['contactemail']
        comessage=request.POST['contactmessage']
        data=Contactdb(contact_name=coname,contact_email=coemail,contact_message=comessage)
        data.save()
    return redirect('userindex')

def productdetails(request,productid):
    data=Productdb.objects.filter(id=productid)
    cartcount=Cart.objects.all().count()
    return render(request,"productdetails.html",{"data":data,"cartcount":cartcount})

def addtocart(request,productid):
    if 'uid' in request.session:
        Quantity=request.POST['qt']
        totalamount=request.POST['totalamt']
        userid=request.session.get('uid')
        product=Productdb.objects.get(id=productid)
        user=Registerb.objects.get(id=userid)
        data=Cart(userid=user,productid=product,quantity=Quantity,total=totalamount,status=0)
        data.save()
        return redirect('usercart')
    else:
        messages.error(request,'please login')
        return redirect('ulogin')