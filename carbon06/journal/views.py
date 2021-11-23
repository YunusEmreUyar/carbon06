from django.shortcuts import render
from .models import Journal, Contributor
from django.views.generic.list import ListView

# Create your views here.
def indexView(request):
	context = {"journals": Journal.objects.all().order_by("-magazine_id")}
	return render(request, "index.html", context)

def detailView(request, id):
	context = {"journal": Journal.objects.get(magazine_id=id)}
	return render(request, "detail.html", context)

class ContributorView(ListView):
	model = Contributor
	template_name = "contributors.html" # This html does not extended from base.html because no need to use bootstrap.
	ordering = ["-role__priority"]