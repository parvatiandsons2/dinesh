from django.db import models

# Create your models here.

class Products(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = "media/")
    price = models.DecimalField(max_digits= 4, decimal_places=2)
