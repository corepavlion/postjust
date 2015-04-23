from django.contrib import admin
from blog.models import BlogPost
from blog.models import BlogCategory
from django.db import models
from tinymce.models import HTMLField


class BlogCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'slug']}),
        ('Published Information', {'fields': ['date','published']}),
    ]
    list_display = ('title', 'published', 'date')

admin.site.register(BlogCategory, BlogCategoryAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,		{'fields': ['title', 'slug','teaser', 'content','categories']}),
        ('Published Information', {'fields': ['date','published']}),
    ]
    search_fields = ['title','date']
    list_display = ('title', 'published', 'date')
    content = HTMLField()

admin.site.register(BlogPost, BlogPostAdmin)
