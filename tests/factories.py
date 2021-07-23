import factory
from faker import Faker
from circle.apps.promo.models import Promo


faker = Faker()


class PromoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Promo
    title = 'Promo Hari Ini'


# class CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Category
#     name = 'helo'
