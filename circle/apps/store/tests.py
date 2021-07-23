# from django.test import TestCase

# from .models import Category, Partner, Product


# class ProductTestCase(TestCase):
#     def setUp(self):
#         Partner.objects.create(id=1, name="Test Partner")
#         Category.objects.create(id=1, name="Test Category")
#         category = Category.objects.get(id=1)
#         partner = Partner.objects.get(id=1)
#         Product.objects.create(id=1, name="Test Name",
#                                description="Test Descriptions", partner=partner, category=category)

#     def test_get_absolute_url(self):
#         """ Test get absolute url """
#         test_slug = Product.objects.get(id=1)
#         print(test_slug.__dict__)
#         self.assertIs()
