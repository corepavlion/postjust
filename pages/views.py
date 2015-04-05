from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from pages.models import Page
# Create your views here.


def mainpage(request):
	try:
		currentPage = Page.objects.get(title = "About Me")
		return render(request, 'index.html', {'mainPage' : currentPage})
	except Page.DoesNotExist:
		return HttpResponse('main page')

def page(request, slug):
	currentPage = get_object_or_404(Page, slug = slug)
	return render(request, 'page.html', {'currentPage' : currentPage})
	#return HttpResponse('asdsad')



