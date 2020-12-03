from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('saveReg',views.saveReg,name='saveReg'),
    path('mail',views.mail,name='mail')  

]