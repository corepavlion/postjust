from django.db import models
from django.utils import timezone

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=500)
	slug = models.SlugField(unique=True)
	published = models.BooleanField(default=True)
	content = models.TextField()
	date = models.DateTimeField('Publised Date', default = timezone.now())
	def __str__(self):
   	    return self.title