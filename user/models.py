from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.IntegerField(null=True)
    image = models.ImageField(upload_to = 'profile_images/')
    service = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.username

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
