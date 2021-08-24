from django.conf import settings
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

from circle.apps.core.models import CoreBaseModel
from circle.apps.partner.models import Partner


class Store(CoreBaseModel):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=80, blank=True)
    logo_image = models.ImageField(upload_to='store/', blank=True)


class Category(CoreBaseModel):
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])


class Product(CoreBaseModel):
    PRODUCT_ATTRIBUTE = [
        ('reg', 'Regular'),
        ('new', 'New'),
        ('pop', 'Popular')
    ]
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    product_code = models.CharField(max_length=80, default='no_code')
    logo_image = models.ImageField(upload_to='product/', blank=True)
    description = HTMLField()
    is_digital = models.BooleanField(default=True)
    attribute = models.CharField(max_length=3, choices=PRODUCT_ATTRIBUTE, default='reg')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])


class Item(CoreBaseModel):
    ITEM_ATTRIBUTE = [
        ('reg', 'Regular'),
        ('new', 'New'),
        ('pop', 'Popular')
    ]
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=120, unique=True)
    buy_price = models.FloatField(default=0, blank=False)
    sell_price = models.FloatField(default=0, blank=False)
    attribute = models.CharField(max_length=3, choices=ITEM_ATTRIBUTE, default='reg')

    class Meta:
        ordering = ('sell_price',)
        index_together = (('id', 'item_code'),)

    def get_margin(self) -> float:
        margin = self.sell_price - self.buy_price
        return margin
