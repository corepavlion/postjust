from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def blogPostList(request):
	postList = BlogPost.objects.all().order_by('-id')[:5]
	return render(request, 'blogMainPage.html', {'postList' : postList})

def blogDetailPage(request, slug):
	blogPost = get_object_or_404(BlogPost, slug = slug)
	return render(request, 'blogDetailPage.html', {'post' : blogPost})
