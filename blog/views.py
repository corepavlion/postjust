from django.shortcuts import render
from blog.models import BlogPost,BlogCategory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def blogPostList(request):
	postList = BlogPost.objects.all().order_by('-id')[:5]
	categories = getCategories()
	return render(request, 'blogMainPage.html', {'postList' : postList, 'categories' : categories})

def blogDetailPage(request, slug):
	blogPost = get_object_or_404(BlogPost, slug = slug)
	return render(request, 'blogDetailPage.html', {'post' : blogPost})

def getCategories():
	return BlogCategory.objects.all()



