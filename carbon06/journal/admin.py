from django.contrib import admin
from .models import Journal

# Register your models here.
class JournalAdmin(admin.ModelAdmin):
	list_display = ["magazine_id", "title", "subtitle"]


admin.site.register(Journal, JournalAdmin)