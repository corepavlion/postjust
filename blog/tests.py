from django.test import TestCase
from .models import BlogPost, BlogCategory

class BlogPostMethodTests(TestCase):

    def test_category_count(self):
        category = BlogCategory()
        category.title = 'test'
        category.save()

        blogPost = BlogPost()
        blogPost.title = 'test'
        blogPost.save()

        blogPost.categories.add(category)

        self.assertEqual(blogPost.categories.all().count(), 1)
