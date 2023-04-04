from django.contrib import admin
from .models import Contactdb
from .models import Registerb
from .models import Cart
from .models import Checkout

# Register your models here.
admin.site.register(Contactdb)
admin.site.register(Registerb)
admin.site.register(Cart)
admin.site.register(Checkout)