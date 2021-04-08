from django.contrib import admin

# Register your models here.
from .models import Products,Category, SubCategory

class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'image', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name']

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Products,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubcategoryAdmin)
