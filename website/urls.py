
from django.contrib import admin
from django.urls import path
from .views import contactbyID, contactus
urlpatterns = [
    path('', contactus),
    path('<int:id>/', contactbyID),
]
