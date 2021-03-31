from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class ContactUs(models.Model):

    objects = models.Manager() # CRUD

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=12, unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'


    def __str__(self):
        return self.name

class BlogCategory(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True, editable=True)

    def __str__(self):
        return self.name

class Blog(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=250)
    url = models.SlugField(max_length=250, editable=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, limit_choices_to={'is_active':True})
    is_active = models.BooleanField(default=True, editable=True)

    def __str__(self):
        return self.name
