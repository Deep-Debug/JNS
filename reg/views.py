from django.shortcuts import render,redirect
from django.http import HttpResponse
from frds import settings  
from django.core.mail import send_mail  
from .models import Registration
from django.template import loader


# Create your views here.

def index(request):
     return render(request,'reg.html',{'display':'none'})



def mail(context):
    subject = "Registration"  
    html_message = loader.render_to_string(
            'mail.html',
            {              
                
            }
        )
		
    msg=""

    
    to      = context['emailid']  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)      



def saveReg(request):

    if request.method == "POST":  
        firstname=request.POST.get('firstname','')
        lastname=request.POST.get('lastname','')
        username=request.POST.get('username','')
        emailid=request.POST.get('emailid','')
        password=request.POST.get('password','')
        rpassword=request.POST.get('rpassword','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')
        

        print('ddddd')
        context={'firstname':firstname,'lastname':lastname,'emailid':emailid,'password':password,'city':city,'zip':zipcode,'state':state,'username':username}
        try:
            R=Registration.objects.get(username=username)
            if(R.emailid==emailid):
                print('1 if')
                print(R)
                print(username)
                print('already register')
                return redirect('/login')
            else:
                print('1 else')
                return render(request,'reg.html',{'display':'block'})
        except:
            if password==rpassword:
                print('2 if')
                R=Registration(firstname=firstname,lastname=lastname,
                username=username,emailid=emailid,password=password,city=city,
                state=state,zipcode=zipcode)
                R.save()
                mail(context)
            else:
                print('2 else')
                print("plz check your pass...")
                return render(request,'reg.html',context) 
        else:
            return redirect('/')
    return render(request,'mail.html',context)


    



        
    
     

