from django.shortcuts import render
from .models import Journal

# Create your views here.
def indexView(request):
	context = {"journals": Journal.objects.all().order_by("-magazine_id")}
	return render(request, "index.html", context)

def detailView(request, id):
	context = {"journal": Journal.objects.get(magazine_id=id)}
	return render(request, "detail.html", context)