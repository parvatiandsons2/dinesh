from django.db import models

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