from django.shortcuts import render,redirect,HttpResponse
from contact.models import Contact
from django.core.mail import send_mail
from . import settings


def index(request):
    return render(request,'index.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        msg = request.POST.get('msg')
        
        contact = Contact(name=name,email=email,sub=sub,msg=msg)
        contact.save()
        
        message=f'Hello {name}. Thank you for connecting with me. I will reply you soon on you message.'
        subject="Mail from Yuvraj Verma"
        send_mail_to(request,email,message,subject)
        
        message=f'Hello Yuvraj you got a mail from {email}. Sub = {sub} , message= {msg}.'
        subject="Mail from Portfolio contact"
        send_mail_to(request,"yuvrajv0504@gmail.com",message,subject)     
        
    return render (request,'index.html')


def send_mail_to(request,email,message,sub):
    send_mail(sub,message,settings.EMAIL_HOST_USER,[email,])
    
    return render(request,'index.html')

    
    

        