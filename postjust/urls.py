from django.conf.urls import patterns, include, url
from django.contrib import admin
import blog.urls
import pages.urls
from pages import views

urlpatterns = patterns('',
	#url(r'^$',include(pages.urls)),
	url(r'^$', views.mainpage, name ='mainPage'),
	url(r'^page/', include(pages.urls)),
	url(r'^blog/', include(blog.urls)),
 	url(r'^admin/', include(admin.site.urls)),
 	(r'^tinymce/', include('tinymce.urls')),
)


