from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .models import Category, Partner, Product, Store


class ModelTesting(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='udjango', password='abcd123')
        self.store = Store.objects.create(owner=self.user)
        self.category = Category.objects.create(name='django', code='django', slug='django')
        self.product = Product.objects.create(name='pdjango', product_code='pdjango',
                                              slug='pdjango', category=self.category, store=self.store)

    def test_post_model(self):
        u = self.user
        self.assertTrue(isinstance(u, User))
        self.assertEqual(str(u), 'udjango')
        d = self.category
        self.assertTrue(isinstance(d, Category))
        self.assertEqual(str(d), 'django')
        p = self.product
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(str(p), 'pdjango')

    def test_get_absolute_url(self):
        self.cslug = Category.objects.get(id=1)
        self.assertEqual('/toko/django/', self.cslug.get_absolute_url())
