from django.shortcuts import render
from django.http import HttpResponse
from frds import settings  
from django.core.mail import send_mail  
from login.models import Login
from django.template import loader
from reg.models import Registration
import random
import math
import datetime

def login(request):
    return render(request,'login.html')


def checklogin(request):
    print('HI')
    if request.method == "POST":

        emailid=request.POST.get('emailid','')
        password=request.POST.get('password','')
        id=request.POST.get('id','')
        #select * from Register where emailid=emailid   
        Registrations_E=Registration.objects.get(emailid=emailid)
        if(Registrations_E.password==password and Registrations_E.emailid==emailid):
            o=random.randrange(100000,999999)
            otp=str(o)
            print(otp) 
            lo=Login(emailid=emailid,password=password,activeotp=True,otp=otp)
            lo.save()
            context={'otp':otp,'emailid':emailid,'password':password}
            print("data added sucessfully...")
            mail(context)
        else:
            print("Data not added.....")
            return render(request,'login.html')
    return render(request,'otp.html',context)


def checkotp(request):
    emailid=request.POST.get('emailid','')
    otp=request.POST.get('otp','')
    print(emailid)
    logins=Login.objects.get(emailid=emailid)

    
    if(logins.activeotp==True and logins.otp==otp):
        logins.activeotp=False
        time=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        #print(time)
        logins.lastlogin=str(time)
        logins.save()
        
        subject = "Login detected"  
        html_message = loader.render_to_string(
            'logindetect.html',
            {          
                
                'lastlogin':logins.lastlogin
            }   
        )
        msg="Your last login is done on "+logins.lastlogin+" Not done by you contact us "

    
        to      = emailid  
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    
        msg="login succesfully"
        print(msg)
        r=Registration.objects.get(emailid=emailid)
        username=r.username
        request.session['uname'] = r.username
        context={'username':username}
        return render(request,'afterlogin.html',context)
    else:
        context={'emailid':emailid}
        return render(request,'otp.html',context)

def mail(context):
    subject = "OTP For Login into JAN SAMSYA NIAVARAN"  
    msg=""
    html_message = loader.render_to_string(
            'sendotp.html',
            {          
                
                'otp':context['otp']
            }
        )    
    to      = context['emailid']  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  

def resetpass(request):
    return render(request,'resetpass.html')

def checkresetpass(request):
    emailid=request.POST.get('emailid','')
    password=request.POST.get('password','')
    repassword=request.POST.get('repassword','')
    l=Login.objects.get(emailid=emailid)
    r=Registration.objects.get(emailid=emailid)
    if(l.emailid==emailid):
        print('email found...')
        if(password==repassword):
            print('pass same')
            r.password=password
            l.password=password
            r.save()
            l.save()
        else:
            print('plz check pass...')
            return render(request,'resetpass.html')
    else:
        print('this emailid is not in database...')
    return render(request,'login.html')

