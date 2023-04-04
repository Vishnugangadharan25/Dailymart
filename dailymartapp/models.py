from django.db import models

# Create your models here.
class Categorydb(models.Model):
    Cname=models.CharField(max_length=150)
    Cimage=models.ImageField()
    Cdescription=models.TextField()
class Productdb(models.Model):
    pr_name=models.CharField(max_length=200)
    pr_price=models.IntegerField()
    pr_weight=models.IntegerField()
    pr_image=models.FileField()
    categories=models.CharField(max_length=200)