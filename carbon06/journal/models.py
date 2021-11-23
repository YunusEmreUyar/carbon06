from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.


class Journal(models.Model):
	magazine_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=100, null=True)
	url = models.URLField(max_length=200, default="")
	cover = models.URLField(max_length=200)
	description = models.TextField()
	article_published = models.DateTimeField(default=datetime.now())

	def __str__(self):
	    return f"carbon06 {self.title}"


class Role(models.Model):
	name = models.CharField(max_length=100)
	priority = models.PositiveIntegerField()
	isWide = models.BooleanField(default=False)

	def __str__(self):
		return self.name



class Contributor(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	personal_link = models.CharField(max_length=255, null=True, blank=True)	
	bio = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to="profiles/")

	def __str__(self):
		return f"{self.name} {self.surname}"
