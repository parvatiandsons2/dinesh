from django.contrib import admin
from .models import ContactUs, BlogCategory, Blog
from django.utils.text import slugify
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):

    list_display=['name','mobile']
    search_fields =['name']
    list_filter = ['mobile']


class BlogCategoryAdmin(admin.ModelAdmin):

    list_display=['name', 'is_active']
    search_fields =['name']
    list_filter = ['is_active']
    # list_editable = ['is_active',]


class BlogAdmin(admin.ModelAdmin):

    list_display=['name','url', 'category', 'is_active']
    search_fields =['name', 'category__name']
    list_filter = ['is_active']

    def save_model(self, request, obj, form, change):
        obj.name= obj.name.trim()
        obj.url = slugify(obj.name)
        return super().save_model(request, obj, form, change)

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)