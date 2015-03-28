from django.contrib import admin
from blog.models import BlogPost
from blog.models import BlogCategory
from blog.models import Page

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

admin.site.register(BlogPost, BlogPostAdmin)


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'slug', 'content','categories']}),
        ('Published Information', {'fields': ['date','published']}),
    ]
    list_display = ('title', 'published', 'date')

admin.site.register(Page, PageAdmin)

