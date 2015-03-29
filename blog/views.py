from django.shortcuts import render
from blog.models import Page
from django.http import HttpResponse

# Create your views here.

def page(request, slug):
	currentPage = Page.objects.get(slug = slug)
	return render(request, 'blog/page.html', {'currentPage' : currentPage})
	#return HttpResponse('asdsad')


	

