from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from pages import views

urlpatterns = patterns('',
	url(r'^(?P<slug>\S+)/', views.page, name ='page')
)
