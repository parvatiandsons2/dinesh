from django.contrib import admin
from .models import ContactUs, BlogCategory, Blog
from django.utils.text import slugify
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):

    list_display=['name','mobile', 'both']
    search_fields =['name']
    list_filter = ['mobile']


class BlogCategoryAdmin(admin.ModelAdmin):

    list_display=['name', 'is_active','created_by', 'created_on']
    search_fields =['name']
    list_filter = ['is_active']


    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            oldImg = BlogCategory.objects.get(pk=obj.pk)
            if(oldImg.image!=obj.image):
                deleteFile(oldImg.image.path)

        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj):
        deleteFile(obj.image.path)
        return super().delete_model(request, obj)

    # list_editable = ['is_active',]


def deleteFile(url):
    import os
    print(os.path.exists(url))
    if(os.path.exists(url)):
        os.remove(url)

class BlogAdmin(admin.ModelAdmin):

    list_display=['name','url', 'category', 'is_active', 'combo_name']
    search_fields =['name', 'category__name']
    list_filter = ['is_active','category']

    def combo_name(self, obj):
        return obj.name+'-'+obj.category.name

    def save_model(self, request, obj, form, change):
        obj.name= obj.name.trim()

        obj.url = slugify(obj.name)
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj):
        return super().delete_model(request, obj)

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)