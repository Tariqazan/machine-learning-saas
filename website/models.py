from django.db import models
from django.urls import reverse
from django.contrib.sitemaps import ping_google

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    file = models.FileField(upload_to='blog/files/',blank=True,null=True)
    date = models.DateTimeField(auto_now=True)

    def save(self,force_insert=False,force_update=False):
        super().save(force_insert,force_update)
        try:
            ping_google('/sitemap.xml','https://www.google.com/webmasters/tools/ping',sitemap_uses_https =False)
        except Exception:
            pass

    def get_absolute_url(self):
        return reverse("blog")
    

class CareerCV(models.Model):
    email = models.EmailField()
    cv = models.FileField(upload_to='career/cv/')
    date = models.DateTimeField(auto_now=True)

    def save(self,force_insert=False,force_update=False):
        super().save(force_insert,force_update)
        try:
            ping_google('/sitemap.xml','https://www.google.com/webmasters/tools/ping',sitemap_uses_https =False)
        except Exception:
            pass

    def get_absolute_url(self):
        return reverse("career")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveBigIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse("index")