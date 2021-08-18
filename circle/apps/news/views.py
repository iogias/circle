import os

import httpx
from django.conf import settings


async def async_get_latest_news():
    params = {'per_page': 10}
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