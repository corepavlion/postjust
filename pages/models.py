from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=500)
	slug = models.SlugField(unique=True)
	published = models.BooleanField(default=True)
	content = HTMLField()
	date = models.DateTimeField('Publised Date', default = timezone.now())
	def __str__(self):
		    return self.title