from email import message
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'demowebsite/index.html')
def about(request):
    return render(request,'demowebsite/about.html')
def userlogin(request):
    return render(request,'demowebsite/userlogin.html')
def bookappointment(request):
    return render(request,'demowebsite/bookappointment.html')
def studentlogin(request):
    return render(request,'demowebsite/studentlogin.html')
def counsellorlogin(request):
    return render(request,'demowebsite/counsellorlogin.html') 
def signup(request):
    return render(request,'demowebsite/signup.html')  
def register(request):
    sid = request.POST['sid']
    name = request.POST['name']
    sem = request.POST['sem']
    dname = request.POST['dname']
    email = request.POST['email']
    pin = request.POST['pin']
    phno = request.POST['phno']

    user = Sregistered.objects.filter(sid=sid)

    if user:
        message = "you already have a Account"
        return render(request,'demowebsite/studentlogin.html',{'msg':message})
    else:
        newuser = Sregistered.objects.create(sid=sid,name=name,sem=sem,dname=dname,email=email,pin=pin,phno=phno)
        message = "registered successfull"
        return render(request,'demowebsite/studentlogin.html',{'msg':message})


def slogin(request):
    sid = request.POST['sid']
    pin = request.POST['pin']

    user = Sregistered.objects.filter(pin=pin,sid=sid)

    if user:
        return render(request,'demowebsite/studenthome.html')
    else:
        message = "wrong entry ...do you have a account?"
        return render(request,'demowebsite/userlogin.html',{'msg':message}) 


def clogin(request):
    cid = request.POST['cid']
    key = request.POST['key']

    cuser = Counsellor.objects.filter(cid=cid,key=key)

    if cuser:
        return render(request,'demowebsite/counsellorhomepage.html')
    else:
        message = "wrong entry ...do you have a account?"
        return render(request,'demowebsite/userlogin.html',{'msg':message})


def fixappointment(request):
    contact = request.POST['contact']
    s_email = request.POST['s_email']
    mssgs = request.POST['mssgs']
    s_name = request.POST['s_name']
    student_id = request.POST['student_id']
    
    
    user = Sregistered.objects.filter(sid=student_id)

    if user:
        newfix = Appointment.objects.create(contact=contact,s_email=s_email,mssgs=mssgs,s_name=s_name,student_id=student_id)
        message = "appointment succesfull , Counsellor will revert you back"
        return render(request,'demowebsite/studenthome.html',{'msg':message})
    else:
        message = "sid was not registered .Insert a valid SID"
        return render(request,'demowebsite/studenthome.html',{'msg':message})



    







