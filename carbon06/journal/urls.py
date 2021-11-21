from django.urls import path
from .views import indexView, detailView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import JournalSitemap, StaticSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'blog':JournalSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path("", indexView, name="index"),
    path("<int:id>/", detailView, name="detail"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
