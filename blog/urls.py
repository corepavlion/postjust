from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blogPostList, name ='blogPostList'),
	url(r'^(?P<category>\S+)/(?P<slug>\S+)/$', views.blogDetail, name ='blogPostDetail'),
	url(r'^(?P<category>\S+)/$', views.blogPostListByCategory, name ='blogPostByCategory'),


)
