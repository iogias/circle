from __future__ import absolute_import, unicode_literals

import os
import httpx
from celery import shared_task
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.text import slugify

from circle.apps.store.models import Item, Partner, Product

# YODU GET PRODUCT #
URL_PRODUCT = 'https://middleware-api.yodu.id/'


def fetch_product_yodu(arg):
    category = arg.upper()
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
            return {"msg": "Fetch Product from YODU failed"}


@shared_task
def save_data_product(arg):
    data = fetch_product_yodu(arg)
    cat_id = 1 if arg.upper() == 'DIRECT' else 2
    for row in data:
        if row['status'] == 'ACTIVE':
            try:
                obj = Product.objects.get(product_code=row['product_id'])
            except Product.DoesNotExist:
                obj = Product(
                    name=row['name'],
                    slug=slugify(row['name']),
                    store_id=1,
                    category_id=cat_id,
                    product_code=row['product_id']
                )
                obj.save()
            return obj


def fetch_items_yodu(arg):
    headers = {'Content-type': 'application/json'}
    params = dict(
        page=0,
        category=arg,
        merchant_label='DEALOKA',
        fk_wallet_id='08111019806',
        fk_user_id='6032097562b332c4902c0a0c',
        token='343a6444d996d9d434d48d776c21071c5f783e300b0c8d35d088c156b0cac4cd',
        dlk_code='MDLK_1614334356_68653331',
        phone_id='07ce0f96366c03c5'
    )
    with httpx.Client() as client:
        url = os.path.join(URL_PRODUCT, 'api_get_product')
        res = client.post(url, headers=headers, params=params)
        if res.status_code == 200:
            result = res.json()
            if result['message_data']['product_list']:
                return result['message_data']['product_list']
        else:
            return {"msg": "Not found"}


@shared_task
def save_data_items():
    products = get_list_or_404(Product, is_active=True)
    products_list = [(pd.id, pd.product_code) for pd in products]
    for p in products_list:
        row = fetch_items_yodu(p[1])
        for r in row:
            product_obj = get_object_or_404(Product, product_code=r['category'])
            partner_obj = get_object_or_404(Partner, code=r['supplier'].lower())

            try:
                obj = Item.objects.get(item_code=r['product_id'].strip(), product_id=p[0])
                break
            except Item.DoesNotExist:
                obj = Item(
                    name=r['name'],
                    slug=slugify(r['name']),
                    item_code=r['product_id'].strip(),
                    buy_price=r['buy_price'],
                    sell_price=r['sale_price'],
                    product_id=product_obj.id,
                    partner_id=partner_obj.id
                )
                obj.save()
            return obj
