from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path("",views.index,name='index'),
    path("home/",views.index,name='index'),
    path("pay/",views.pay,name='pay'),
    path("addcus2/",views.addcus2,name='addcus2'),
    path("addcus/",views.addcus,name='addcus'),
    path("tfs/",views.transfers,name='trfs')
       
]