from django.db import models
from dailymartapp.models import Productdb
# Create your models here.
class Contactdb(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.EmailField()
    contact_message=models.CharField(max_length=500)

class Registerb(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    phonenum=models.IntegerField()

class Cart(models.Model):
    userid=models.ForeignKey(Registerb, on_delete=models.CASCADE)
    productid=models.ForeignKey(Productdb, on_delete=models.CASCADE)
    status=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()

class Checkout(models.Model):
    fname=models.CharField(max_length=55)
    lname=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    saddress=models.CharField(max_length=300)
    pcode=models.IntegerField()
    city=models.CharField(max_length=50)
    cemail=models.EmailField()
    cphone=models.IntegerField()
    userid=models.ForeignKey(Registerb, on_delete=models.CASCADE)
    cartid=models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)