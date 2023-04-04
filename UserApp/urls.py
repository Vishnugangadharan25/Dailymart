from django.urls import path
from . import views

urlpatterns=[
    path('userindex/',views.userindex,name='userindex'),
    path('userabout/',views.userabout,name='userabout'),
    path('usercart/',views.usercart,name='usercart'),
    path('usercheckout/',views.usercheckout,name='usercheckout'),
    path('usercontact/',views.usercontact,name='usercontact'),
    path('usershop/<str:cat>/',views.usershop,name='usershop'),
    path('useregister/',views.useregister,name='useregister'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('productdetails/<int:productid>/',views.productdetails,name='productdetails'),
    path('contactdata/',views.contactdata,name='contactdata'),
    path('registerpage/',views.registerpage,name='registerpage'),
    path('ulogin/',views.ulogin,name='ulogin'),
    path('addtocart/<int:productid>/',views.addtocart,name='addtocart'),
    path('checkout/',views.checkout,name="checkout"),
    path('cartupdate/',views.cartupdate,name='cartupdate')
]