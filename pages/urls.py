from django.conf.urls import patterns, include, url
from pages import views

urlpatterns = patterns('',
	url(r'^(?P<slug>\S+)/', views.page, name ='page')
)
