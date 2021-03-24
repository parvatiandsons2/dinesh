from django.shortcuts import render
from django.contrib import messages
from website.models import ContactUs
# Create your views here.

def contactus(request):
    try:
        __context={}
        if request.method =='POST':
            print(request.POST)
            ContactUs.objects.create(name=request.POST['name'],
            mobile=request.POST['mobile'],email=request.POST['email'],
            subject=request.POST['subject'],message=request.POST['message']
            )

            messages.add_message(request, messages.SUCCESS, 'Data Saved!')
        
        data = ContactUs.objects.all()

        __context['Contacts']=data

        return render(request, 'index.html', __context)
    except Exception as ex:
        messages.add_message(request, messages.ERROR, ex)
        return render(request, 'index.html')