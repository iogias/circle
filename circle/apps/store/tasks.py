from __future__ import absolute_import, unicode_literals

import os

import httpx
from celery import shared_task
from django.utils.text import slugify

from circle.apps.store.models import Product

# YODU GET PRODUCT #
URL_PRODUCT = 'https://middleware-api.yodu.id/'


def fetch_product_yodu(param):
    category = param.upper()
    headers = {'Content-type': 'application/json'}
    params = dict(
        result_per_page=100,
        page=1,
        category=category,
        merchant_label='DEALOKA',
        fk_user_id='603f16d83fc541ecae437e09',
        token='25cffd0c186e9beb7d9855d5023ca0a5c6e12f1d23a9c2c2902e9714e0fde3dd',
        dlk_code='MDLK_1626061817_13409410',
        phone_id='aa2930a0ab7157e0'
    )
    with httpx.Client() as client:
        url = os.path.join(URL_PRODUCT, 'api_get_product_group_url')
        res = client.post(url, headers=headers, params=params)
        if res.status_code == 200:
            result = res.json()
            if result['message_data']['product_group_list']:
                return result['message_data']['product_group_list']
        else:
            return {"msg": "Not found"}


@shared_task
def get_data_product(arg):
    data = fetch_product_yodu(arg)
    cat_id = 1 if arg.upper() == 'DIRECT' else 2
    for row in data:
        if row['status'] == 'ACTIVE':
            obj, created = Product.objects.update_or_create(
                name=row['name'],
                slug=slugify(row['name']),
                store_id=1,
                category_id=cat_id,
                product_code=row['product_id'],
                logo_image=row['image'],
                defaults={"product_code": row['product_id']}
            )

            # try:
            #     obj = Product.objects.get(product_code=row['product_id'])
            # except Product.DoesNotExist:
            #     obj = Product(
            #         name=row['name'],
            #         slug=slugify(row['name']),
            #         store_id=1,
            #         category_id=cat_id,
            #         product_code=row['product_id'],
            #         logo_image=row['image']
            #     )
            #     obj.save()
            # obj, created = Product.objects.get_or_create(
            #     name=row['name'],
            #     slug=slugify(row['name']),
            #     store_id=1,
            #     category_id=cat_id,
            #     product_code=row['product_id'],
            #     defaults={'product_code': row['product_id']}
            # )

            # return created

        # @shared_task
        # async def gets_product_yodu(category):
        #     headers = {'Content-type': 'application/json'}
        #     params = dict(
        #         result_per_page=100,
        #         page=1,
        #         category=category,
        #         merchant_label='DEALOKA',
        #         fk_user_id='603f16d83fc541ecae437e09',
        #         token='25cffd0c186e9beb7d9855d5023ca0a5c6e12f1d23a9c2c2902e9714e0fde3dd',
        #         dlk_code='MDLK_1626061817_13409410',
        #         phone_id='aa2930a0ab7157e0'
        #     )
        #     async with httpx.AsyncClient() as client:
        #         url = os.path.join(URL_PRODUCT, 'api_get_product_group_url')
        #         res = await client.post(url, headers=headers, params=params)
        #         if res.status_code == 200:
        #             result = res.json()
        #             if result['message_data']['product_group_list']:
        #                 filtered_result = [r for r in result['message_data']['product_group_list']]
        #                 cat_id = 1 if category == 'DIRECT' else 2
        #                 for row in result['message_data']['product_group_list']:

        #                     obj, created = Product.objects.update_or_create(
        #                         name=row['name'],
        #                         store_id=1,
        #                         partner_id=1,
        #                         category_id=cat_id,
        #                         product_code=row['product_id'],
        #                         defaults={'name': 'Free Fire'}
        #                     )
        #                 return filtered_result
        #         else:
        #             return {"msg": "Not found"}
