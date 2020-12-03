from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.aftlogin,name='aftlogin'),
    path('Dashboard',views.loadDashboard,name='loadDashboard'),
    path('help',views.help,name='help'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('logout',views.logout,name='logout'),
    path('Complain',views.loadComplain,name='loadComplain'),
    path('loadmyaccount',views.loadmyaccount,name='loadmyaccount'),
    path('updatemyaccount',views.updatemyaccount,name='updatemyaccount'),
    path('saveComplain',views.saveComplain,name='saveComplain'),
    path('updatecomplain/<str:Complain_id>',views.updatecomplain),
    path('deletecomplain/<str:Complain_id>',views.deletecomplain),
    path('updateComplain2',views.updateComplain2,name='updateComplain2'),

]