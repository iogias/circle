from django.db import models
from django.utils import timezone


class CoreBaseModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CoreNoNameModel(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
