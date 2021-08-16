from django.urls import path
from .views import indexView, detailView

urlpatterns = [
    path("", indexView, name="index"),
    path("<int:id>/", detailView, name="detail"),
]
