import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone
from tinymce.models import HTMLField

from circle.apps.core.models import CoreNoNameModel


class Promo(CoreNoNameModel):
    BANNER_TYPE = [('hero', 'Hero'), ('popup', 'Popup')]
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = HTMLField()
    banner_img = models.ImageField(upload_to='promo/%Y/%m', blank=True)
    banner_type = models.CharField(max_length=8, choices=BANNER_TYPE, default='hero')
    started = models.DateTimeField(default=timezone.now)
    ended = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'),)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> None:
        return reverse('promo:promo_detail', args=[self.id, self.slug])

    def get_ongoing_promo(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.ended <= now
