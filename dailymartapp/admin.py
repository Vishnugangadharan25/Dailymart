from django.contrib import admin
from . import models
from . models import Categorydb
from . models import Productdb
# Register your models here.
admin.site.register(Categorydb)
admin.site.register(Productdb)