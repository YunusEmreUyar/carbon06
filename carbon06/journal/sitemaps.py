from django.contrib.sitemaps import Sitemap
from .models import Journal, Contributor
from django.urls import reverse

class JournalSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    protocol = 'http'

    def items(self):
        return Journal.objects.all()

    def lastmod(self, obj):
        return obj.article_published

    def location(self,obj):
        return '/' + str(obj.pk)

class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = 'http'

    def items(self):
        return ['index', 'contributors']

    def location(self, item):
        return reverse(item)
