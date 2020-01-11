import datetime

from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date', )

    def published_recently(self):
        now = timezone.now()
        two_days_ago = now - datetime.timedelta(days=2)
        return two_days_ago < self.publish_date <= now

    def __str__(self):
        return self.title
