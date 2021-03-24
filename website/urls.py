
from django.contrib import admin
from django.urls import path
from .views import contactus
urlpatterns = [
    path('', contactus),
]
