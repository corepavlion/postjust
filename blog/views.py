from django.shortcuts import render
from blog.models import BlogPost, BlogCategory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def blogPostList(request):
	postList = BlogPost.objects.all().order_by('-id')
	categories = getCategories()
	return render(request, 'blogMainPage.html',
		{'postList' : postList, 'categories' : categories})
def blogPostListByCategory(request, category):
	category = 	get_object_or_404(BlogCategory,slug = category)
	postList = category.blogpost_set.all()
	categories = getCategories()
	return render(request, 'blogListPage.html',
		{'postList' : postList, 'categories': categories})
def blogDetail(request,blog_slug):
	blogPost = get_object_or_404(BlogPost, slug = blog_slug)
	blog_categories = blogPost.categories.all()
	categories = getCategories()
	return render(request, 'blogDetailPage.html', {'post' : blogPost,'blog_categories' : blog_categories, 'categories' : categories })

def getCategories():
	return BlogCategory.objects.all()
