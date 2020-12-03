from django.shortcuts import render,redirect
from django.http import HttpResponse
from frds import settings
from login.models import Login
from reg.models import Registration
from afterlogin.models import Complain
# Create your views here.
def aftlogin(request):
    return render(request,'afterlogin.html')

def loadDashboard(request):
    uname = request.session['uname']
    print(uname)
    c = Complain.objects.all().filter(username=uname)
    return render(request,'Dashboard.html',{'context':c})

def loadComplain(request):
    print('oooooooooooooooooooooooooo')
    uname = request.session['uname']
    context = {'action':'/aftlogin/saveComplain'}
    return render(request,'Complain.html',context)


def saveComplain(request):
    print('yyyyyy')
    if request.method == "POST":
        problem= request.POST.get('problem', '')
        description=request.POST.get('description','')
        image=request.FILES['image']
        address=request.POST.get('address','')
        zip=request.POST.get('zip','')
        ward=request.POST.get('ward','')
        uname = request.session['uname']
        print(uname)
        print('in comp..')
        Complaints= Complain(username=uname,problem=problem,description=description, image=image,
                            address=address,zip=zip, ward=ward)
        Complaints.save()
    return render(request,'Complain.html')

def updatecomplain(request,Complain_id):
    complains = Complain.objects.get(Complain_id=Complain_id)
    print(Complain_id)
    print(complains.description)
    print(complains.problem)
    request.session['Complain_id'] = complains.Complain_id
    context = {'complaint':complains,'action':'/aftlogin/updateComplain2'}
    return render(request,'Complain.html',context)

def updateComplain2(request):
    if request.method == "POST":
        problem= request.POST.get('problem', '')
        description=request.POST.get('description','')
        image=request.FILES['image']
        address=request.POST.get('address','')
        zip=request.POST.get('zip','')
        ward=request.POST.get('ward','')
        uname = request.session['uname']
        cid = request.session['Complain_id']
        print(uname)
        print(cid)
        Complains = Complain.objects.filter(Complain_id=cid).update(problem=problem,description=description, image=image,
                            address=address,zip=zip, ward=ward)
        Complain1 = Complain.objects.get(Complain_id=cid)
        Complain1.image=image
        Complain1.save()
    return render(request,'Complain.html')


def deletecomplain(request,Complain_id):
    complains = Complain.objects.get(Complain_id=Complain_id)
    print(Complain_id)
    print(complains.description)
    print(complains.problem)
    complains.delete()
    uname = request.session['uname']
    print(uname)
    c = Complain.objects.all().filter(username=uname)
    return render(request,'Dashboard.html',{'context':c})


def loadmyaccount(request):
    uname = request.session['uname']
    print(uname)
    accounts = Registration.objects.get(username = uname)
    print(accounts.lastname)
    context = {'acc':accounts}
    print(accounts.zipcode)
    return render(request,'myaccount.html',context)


def updatemyaccount(request):
    
    uname = request.session['uname']
    Registrations=Registration.objects.get(username=uname)
    username=Registrations.username
    print(username)
    emailid=Registrations.emailid
    if request.method == "POST":  

        updateusername=request.POST.get('username','')
        updatefirstname=request.POST.get('firstname','')
        updatelastname=request.POST.get('lastname','')
        updatecity=request.POST.get('city','')
        updatestate=request.POST.get('state','')
        updatezipcode=request.POST.get('zip','')
        if(updateusername==username):

            
            Registrations.firstname=updatefirstname
            Registrations.lastname=updatelastname
            Registrations.username= updateusername
            Registrations.city= updatecity
            Registrations.state= updatestate
            Registrations.zipcode= updatezipcode
            Registrations.save()
            
            
            
        elif(updateusername!=username):

            try:
                Registrations=Registration.objects.get(username=updateusername)
                context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':''}
                return render(request,'myaccount.html',context)
            except:
         
                Registrations.firstname=updatefirstname
                Registrations.lastname=updatelastname
                Registrations.username= updateusername
                Registrations.city= updatecity
                Registrations.state= updatestate
                Registrations.zipcode= updatezipcode
                Registrations.save()
                if(Complain.objects.filter(username=username).update(username=updateusername)):
                    pass
                else:
                    pass             
    request.session['uname']=updateusername
    context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':'none'}
    return render(request,'myaccount.html',context)           
                
    
            
                
                

    context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':'none',}
    return render(request,'myaccount.html',context)

                   
def logout(request):
    del request.session['uname']
    return redirect('/aftlogin')
def help(request):
    return render(request,'help.html')

def aboutus(request):
    return render(request,'aboutus.html')
    

        