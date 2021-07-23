import httpx
import os
from circle.apps.core.models import CoreBaseModel
from django.db import models
from django.db.models.fields.json import JSONField


class Payment(CoreBaseModel):
    code = models.CharField(max_length=32, unique=True)
    logo_image = models.ImageField(upload_to='payment', blank=True)
    credentials = JSONField()
    endpoint = JSONField()

    def create_token(self):
        username = self.credentials['username']
        password = self.credentials['password']
        mid = self.credentials['mid']
        prefix = 999
        name = 'Yodu Circle'
        headers = {'Content-type': 'x-www-form-urlencoded'}
        payload = dict(
            username=username,
            password=password,
            mid=mid,
            merchant_name=name,
            merchant_prefix=prefix,
            api_key=mid
        )
        url = os.path.join(self.endpoint['push_pay'], 'create-token')
        client = httpx.Client()
        try:
            r = client.post(url, headers=headers, data=payload)
            r.raise_for_status()
            if r.status_code == 200:
                result = r.json()
                return result
        except httpx.HTTPError as exc:
            return f'Error : {exc}'
        finally:
            client.close()
