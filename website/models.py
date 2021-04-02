from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth import settings
from django.utils.timezone import datetime

# Create your models here.


class ContactUs(models.Model):

    objects = models.Manager() # CRUD

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=12, unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def both(self):
        return self.name+'-'+self.mobile

    class Meta:
        verbose_name_plural = 'Contacts'


    def __str__(self):
        return self.name

class BlogCategory(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True, editable=True)

    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING, editable=False, null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    image = models.ImageField(upload_to="category/", null=True, blank=True)

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
