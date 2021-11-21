from django.db import models
from datetime import datetime
# Create your models here.


class Journal(models.Model):
	magazine_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=100, null=True)
	url = models.URLField(max_length=200, default="")
	cover = models.URLField(max_length=200)
	description = models.TextField()
	article_published = models.DateTimeField(default=datetime.now())
	file = models.FileField(upload_to="static/carbon06", null=True, blank=True)

	def __str__(self):
	    return f"carbon06 {self.title}"

