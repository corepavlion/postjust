from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.blogPostList, name ='blogPostList'),
	url(r'^(?P<slug>\S+)/', views.blogDetailPage, name ='blogDetailPage')
)