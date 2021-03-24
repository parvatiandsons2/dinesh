from django.contrib import admin
from .models import ContactUs
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):

    list_display=['name','mobile']
    search_fields =['name']
    list_filter = ['mobile']

admin.site.register(ContactUs, ContactUsAdmin)