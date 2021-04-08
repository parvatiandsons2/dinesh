
from django.contrib import admin
from django.urls import path
from .views import contactbyID, contactus, index, about, contact, service, blog, feedback, blog_details, productDetails
urlpatterns = [
    path('index/', contactus, name='index_1'),
    path('about/<int:id>/', contactbyID, name='index_2'),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('product/<int:id>/details/', productDetails, name='productDetails'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:url>/details/', blog_details, name='blog_details'),
    path('feedback/', feedback, name='feedback')
]
