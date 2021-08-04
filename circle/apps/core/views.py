import asyncio
import os

import httpx
from django.conf import settings
from django.shortcuts import render

from circle.apps.promo.models import Promo
from circle.apps.store.models import Category, Product

# from circle.apps.store.tasks import get_data_product


def home(request):
    # produk = get_data_product('direct')  # noqa
    # print(">>PRODUK>>", produk)
    categories = Category.objects.filter(is_active=True)
    ongoing_hero = Promo.objects.filter(is_active=True, banner_type='hero')
    pop_products = Product.objects.filter(is_active=True, attribute='pop')
    latest_news = asyncio.run(async_get_latest_news())
    list_cat = []
    if latest_news:
        for cat in latest_news:
            category = asyncio.run(async_get_news_categories(cat['id']))
            list_cat.append(category)
    context = {'ongoing_hero': ongoing_hero,
               'categories': categories,
               'pop_products': pop_products,
               'latest_news': latest_news,
               'list_cat': list_cat}
    return render(request, 'index.html', context)


async def async_get_latest_news():
    params = {'per_page': 8}
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'posts/')
        res = await client.get(url, params=params, timeout=None)

        list_key = ['id', 'title', 'link',
                    'categories', 'jetpack_featured_media_url']
        if res.status_code == 200:
            result = res.json()
            new_result = [
                {key: value for key, value in r.items() if key in list_key}
                for r in result]
            return new_result


async def async_get_news_categories(_id):
    params = {'post': _id}
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'categories')
        res = await client.get(url, params=params, timeout=None)
        if res.status_code == 200:
            result = res.json()
            return dict(id=result[0]['id'], name=result[0]['name'])

# def get_latest_news():
#     params = {'per_page': 8}
#     client = httpx.Client()
#     list_key = ['id', 'title', 'link',
#                 'categories', 'jetpack_featured_media_url']
#     try:
#         url = os.path.join(settings.WP_ENDPOINT, 'posts/')
#         res = client.get(url, params=params)
#         if res.status_code == 200:
#             result = res.json()
#             new_result = [
#                 {key: value for key, value in r.items() if key in list_key}
#                 for r in result]
#             return new_result
#     except httpx.HTTPError as exc:
#         return f'An error occurred while requesting {exc}.'
#     finally:
#         client.close()

# def get_news_categories(_id):
#     params = {'post': _id}
#     client = httpx.Client()
#     try:
#         url = os.path.join(settings.WP_ENDPOINT, 'categories')
#         res = client.get(url, params=params)
#         if res.status_code == 200:
#             result = res.json()
#             return dict(id=result[0]['id'], name=result[0]['name'])
#     except httpx.HTTPError as exc:
#         return f'An error occurred while requesting {exc}.'
#     finally:
#         client.close()


def tentang_kami(request):
    return render(request, 'tentang_kami.html')


def faq(request):
    return render(request, 'faq.html')


def syarat_ketentuan(request):
    return render(request, 'syarat_ketentuan.html')


def kontak_kami(request):
    return render(request, 'kontak_kami.html')
