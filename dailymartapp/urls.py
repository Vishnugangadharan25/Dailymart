from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('form/',views.form,name='form'),
    path('formdata/',views.formdata,name='formdata'),
    path('tabledata/',views.tabledata,name='tabledata'),
    path('tabledit/<int:tableid>/',views.tabledit,name='tabledit'),
    path('updatetable/<int:tableid>/',views.updatetable,name='updatetable'),
    path('deletion/<int:tableid>/',views.deletion,name='deletion'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('productupdate/<int:productid>/',views.productupdate,name='productupdate'),
    path('productdelete/<int:productid>/',views.productdelete,name='productdelete'),
    path('productedit/<int:productid>/',views.productedit,name='productedit'),
    path('productadd/',views.productadd,name='productadd'),
    path('productview/',views.productview,name='productview'),
    path('product/',views.product,name='product'),
    path('messageview/',views.messageview,name='messageview'),
    path('viewuser/',views.viewuser,name='viewuser')
]