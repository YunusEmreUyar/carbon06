from django.db import models

# Create your models here.


class Journal(models.Model):
	magazine_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=100, null=True)
	url = models.URLField(max_length=200, default="")
	cover = models.URLField(max_length=200)
	description = models.TextField()

