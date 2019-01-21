from django.db import models
from django.utils import timezone
# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=50)
	brief = models.CharField(max_length=150)
	description = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
