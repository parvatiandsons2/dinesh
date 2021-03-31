from django.shortcuts import render
from django.contrib import messages
from website.models import ContactUs, Blog, BlogCategory
from django.db.models import Count
from django.db.models import CharField
from django.db.models.functions import Lower

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

        # print(BlogCategory.objects.filter(is_active=True))
        # print(BlogCategory.objects.exclude(is_active=True))

        # print(Blog.objects.select_related('category').get(pk=1))
        # print(BlogCategory.objects.annotate(Count('blog'))[0].blog__count)
        CharField.register_lookup(Lower)
        print(BlogCategory.objects.values('name__lower'))

        __context['Contacts']=data

        return render(request, 'index.html', __context)
    except Exception as ex:
        messages.add_message(request, messages.ERROR, ex)
        return render(request, 'index.html')