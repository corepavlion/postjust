from django.contrib import admin
from blog.models import BlogPost
from blog.models import BlogCategory

class BlogCategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'published', 'date']

admin.site.register(BlogCategory, BlogCategoryAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'teaser', 'content', 'published', 'categories', 'date']

admin.site.register(BlogPost, BlogPostAdmin)

