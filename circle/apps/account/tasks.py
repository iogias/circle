from __future__ import absolute_import, unicode_literals

import os

import httpx
from celery import shared_task
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404

from circle.apps.account.models import Profile

URL_MEMBER = 'https://reporting-api.yodu.id/v1/api/report/'


def fetch_member_yodu(arg):
    headers = {}
    payload = dict(
        start_tm='0',
        end_tm='1655915896490',
        username='api-user',
        password='ap1u53r',
    )
    with httpx.Client() as client:
        url = os.path.join(URL_MEMBER, arg)
        res = client.post(url, headers=headers, data=payload)
        if res.status_code == 200:
            result = res.json()
            return result['wms_user_list']
        else:
            return {"msg": "Fetch Member from YODU failed"}


@shared_task
def save_data_member(arg):
    data = fetch_member_yodu(arg)
    # data[:] = [x for x in data if '-' not in x['wallet_id']]
    for y in data[:]:
        if 'Test' in y['name']:
            data.remove(y)
        elif 'SUPER_MASTER_WALLET' in y['name']:
            data.remove(y)
        elif '-' in y['wallet_id']:
            data.remove(y)

    for row in data:
        is_premium = True if row['premium'] == 'TRUE' else False
        group = get_object_or_404(Group, name='Member')
        values = dict(
            username=row['wallet_id'],
            email=row['email'],
            is_active=False
        )

        try:
            obj = User.objects.get(username=row['wallet_id'], groups=group.id)
        except User.DoesNotExist:
            obj = User(**values)
            obj.save()
            obj.groups.add(group.id)
            Profile.objects.create(user=obj, name=row['name'], premium=is_premium)

    # return obj
