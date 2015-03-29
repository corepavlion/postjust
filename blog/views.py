from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse

# Create your views here.

	

def blogPostList(request):
	return HttpResponse('blogs')
	#return render(request, 'blogMainPage.html', {'currentPage' : currentPage})
