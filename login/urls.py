from django.urls import path
from . import views

urlpatterns = [
   
    path('checklogin',views.checklogin,name='checklogin'),
    path('checkotp',views.checkotp,name='checkotp'),
    path('',views.login),
    path('resetpass',views.resetpass,name='resetpass'),
    path('checkresetpass',views.checkresetpass,name='checkresetpass'),
    

]