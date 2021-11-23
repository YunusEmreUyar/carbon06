from django.urls import path
from .views import indexView, detailView, ContributorView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import JournalSitemap, StaticSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticSitemap,
    'blog':JournalSitemap
}

urlpatterns = [
    path("", indexView, name="index"),
    path("<int:id>/", detailView, name="detail"),
    path("contributors", ContributorView.as_view(), name="contributors"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
