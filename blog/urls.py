from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blogPostList, name ='blogPostList'),
	url(r'^category/(?P<category>\S+)/$', views.blogPostListByCategory, name ='blogPostByCategory'),
	url(r'^(?P<blog_slug>\S+)/$', views.blogDetail, name ='blogPostDetail')
	)
