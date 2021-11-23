from django.contrib import admin
from .models import Journal, Contributor, Role

# Register your models here.
class JournalAdmin(admin.ModelAdmin):
	list_display = ["magazine_id", "title", "subtitle"]

class ContributorAdmin(admin.ModelAdmin):
	list_display = ["name", "surname", "role"]

admin.site.register(Journal, JournalAdmin)
admin.site.register(Role)
admin.site.register(Contributor, ContributorAdmin)