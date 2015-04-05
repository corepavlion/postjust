from django.contrib import admin
from pages.models import Page
from django.db import models
from tinymce.models import HTMLField

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'slug', 'content']}),
        ('Published Information', {'fields': ['date','published']}),
    ]
    list_display = ('title', 'published', 'date')
    content = HTMLField()
  

admin.site.register(Page, PageAdmin)


