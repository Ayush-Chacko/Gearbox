from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Tools(models.Model):
    icon_class = models.CharField(
        max_length=50,
        help_text="Bootstrap icon class, e.g. 'bi-hammer'"
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(..., blank=True, null=True)
    image_url = models.URLField(..., blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name