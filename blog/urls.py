from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
	url(r'^page/(?P<slug>\S+)/', views.page, name ='page')
)
