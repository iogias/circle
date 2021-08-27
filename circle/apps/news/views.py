import os

import httpx
from django.conf import settings


async def async_get_news_by_category(_id, page):
    params = {'categories': _id, 'per_page': page}
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'posts')
        res = await client.get(url, params=params, timeout=None)
        list_key = ['id', 'date', 'title', 'link',
                    'categories', 'jetpack_featured_media_url']
        if res.status_code == 200:
            result = res.json()
            new_result = [
                {key: value for key, value in r.items() if key in list_key}
                for r in result]

            return new_result


async def async_get_news_categories():
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'categories')
        res = await client.get(url, timeout=None)

        list_key = ['id', 'link', 'name', 'description']
        if res.status_code == 200:
            result = res.json()
            new_result = [
                {key: value for key, value in r.items() if key in list_key}
                for r in result]
            return new_result


async def async_get_latest_news():
    params = {'per_page': 10}
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'posts/')
        res = await client.get(url, params=params, timeout=None)

        list_key = ['id', 'date', 'title', 'link', 'slug',
                    'categories', 'jetpack_featured_media_url']
        if res.status_code == 200:
            result = res.json()
            new_result = [
                {key: value for key, value in r.items() if key in list_key}
                for r in result]
            return new_result


async def async_get_news_categories_id(_id):
    params = {'post': _id}
    async with httpx.AsyncClient() as client:
        url = os.path.join(settings.WP_ENDPOINT, 'categories')
        res = await client.get(url, params=params, timeout=None)
        if res.status_code == 200:
            result = res.json()
            return dict(id=result[0]['id'], name=result[0]['name'])
