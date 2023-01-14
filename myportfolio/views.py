from django.shortcuts import render
from contact.models import Contact



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
        print(contact.name)
    
    return render (request,'index.html')


        