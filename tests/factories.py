import factory
from faker import Faker
from circle.apps.promo.models import Promo
from django.utils import timezone

faker = Faker()


class PromoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Promo
    title = 'Promo Hari Ini'
    slug = 'promo-hari-ini'
    banner_img = 'promo_placeholder.jpg'
    ended = timezone.now()


# class CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Category
#     name = 'helo'
