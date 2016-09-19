from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Post(models.Model):
	name = models.CharField(max_length=200)

	published_date = models.DateTimeField(null=True, blank=True)

	bio = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	url = models.URLField(max_length=200)

	def __str__(self):
		return self.name
		return self.url

	def get_absolute_url(self):
		return reverse("blog:post", kwargs={"id": self.pk})

	def is_published(self):
		return self.published_date is not None and self.published_date < timezone.now()

	is_published.boolean = True
	is_published.short_description = "Published?"