from django.contrib.sitemaps import Sitemap
from .models import *

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Blog.objects.all().order_by('-id')

    def lastmod(self, obj):
        return obj.date


class CVSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return CareerCV.objects.all().order_by('-id')

    def lastmod(self,obj):
        return obj.date