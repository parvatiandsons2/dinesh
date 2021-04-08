from django.db import models
from django.db.models.expressions import F

# Create your models here.
class Category(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=120)

class SubCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=120)
    Category = models.ForeignKey(Category , on_delete= models.SET_NULL, null= True, blank= True)


class Products(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = "media/")
    price = models.DecimalField(max_digits= 4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, blank= True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL , null= True , blank=True)

