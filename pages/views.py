from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from pages.models import Page
# Create your views here.

def mainpage(request):
	#currentPage = Page.objects.get(slug = slug)
	#return render(request, 'page.html', {'currentPage' : currentPage})
	return HttpResponse('main page')

def page(request, slug):
	currentPage = get_object_or_404(Page, slug = slug)
	return render(request, 'page.html', {'currentPage' : currentPage})
	#return HttpResponse('asdsad')


