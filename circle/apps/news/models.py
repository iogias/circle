from django.conf import settings
from django.db import models


class UserPosts(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, blank=True, null=True)
    alias = models.CharField(max_length=64, blank=True, unique=True)
    comment_count = models.SmallIntegerField(default=0)
    event = models.CharField(max_length=64, blank=True)
    points = models.IntegerField(default=0)
    link_url = models.URLField(blank=True)
    published = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self) -> str:
        return self.title
