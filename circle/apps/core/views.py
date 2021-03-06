import asyncio

from django.shortcuts import render

from circle.apps.news.views import (async_get_latest_news,
                                    async_get_news_categories_id)
from circle.apps.promo.models import Promo
from circle.apps.store.models import Category, Product


def home(request):
    categories = Category.objects.filter(is_active=True)
    ongoing_hero = Promo.objects.filter(is_active=True, banner_type='hero')
    pop_products = Product.objects.filter(is_active=True, attribute='pop') or Product.objects.filter(
        is_active=True).order_by('-created')

    latest_news = asyncio.run(async_get_latest_news())
    list_cat = []
    if latest_news:
        for cat in latest_news:
            category = asyncio.run(async_get_news_categories_id(cat['id']))
            list_cat.append(category)
    context = {'ongoing_hero': ongoing_hero,
               'categories': categories,
               'pop_products': pop_products,
               'latest_news': latest_news,
               'list_cat': list_cat}
    return render(request, 'index.html', context)


def tentang_kami(request):
    return render(request, 'tentang_kami.html')


def faq(request):
    return render(request, 'faq.html')


def syarat_ketentuan(request):
    return render(request, 'syarat_ketentuan.html')


def kontak_kami(request):
    return render(request, 'kontak_kami.html')
