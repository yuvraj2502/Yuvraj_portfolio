from django.shortcuts import render,redirect,HttpResponse
from contact.models import Contact
from django.core.mail import send_mail, EmailMessage
from . import settings
import threading
from threading import Thread


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
        message=str(message)
        subject="Mail from Yuvraj Verma"
        send_html_mail(subject,message,email)
        
    return render (request,'index.html')


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()