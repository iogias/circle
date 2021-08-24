import hashlib
import json
import random
import string
from datetime import datetime

import httpx
import xmltodict
from django.db import models

from circle.apps.core.models import CoreBaseModel

NOW = datetime.now()
TIME_STAMP = str(round(NOW.timestamp()))


class Partner(CoreBaseModel):
    code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=80, blank=True)
    credentials = models.JSONField(blank=True)
    endpoint = models.JSONField(blank=True)

    # ========= UPOINT =========== #
    def upoint_dtu_inquiry(self, *args):
        if self.code == 'upoint':
            prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            item_code = args[0]
            ref_no = prefix + '_' + item_code
            return ref_no

    def upoint_dtu_payment(self, *args):
        pass

    def upoint_voucher_request(self, *args):
        if self.code == 'upoint_voucher':
            prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            item_code = args[0]
            ref_no = prefix + '_' + item_code
            array_inquiry = [str(self.credentials['partner_id']), ref_no,
                             str(item_code), TIME_STAMP, self.credentials['secret_token']]
            join_sign_inquiry = ''.join(array_inquiry)
            signature_inquiry = (hashlib.md5(join_sign_inquiry.encode('utf-8')).hexdigest()).lower()
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data_request = dict(
                partner_id=self.credentials['partner_id'],
                ref_no=ref_no,
                item_code=item_code,
                timestamp=TIME_STAMP,
                signature=signature_inquiry,
            )
            url = self.endpoint['inquiry']
            client = httpx.Client()
            try:
                r = client.post(url, headers=headers, data=data_request)
                r.raise_for_status()
                if r.status_code == 200:
                    result = r.json()
                    return result
            except httpx.HTTPError as exc:
                return f'Error : {exc}'
            finally:
                client.close()

    def upoint_voucher_payment(self, *kwargs):
        # array_confirm = [str(PARTNER_ID_VOUCHER),
        # response_inquiry["trx_id"],ref_no,str(response_inquiry["status"]),SECRET_TOKEN_VOUCHER]
        if self.code == 'upoint_voucher':
            prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            item_code = kwargs['trx_id']
            trx_id = prefix + '_' + item_code
            array_inquiry = [str(self.credentials['partner_id']), trx_id,
                             str(item_code), TIME_STAMP, self.credentials['secret_token']]
            join_sign_inquiry = ''.join(array_inquiry)
            signature_inquiry = (hashlib.md5(join_sign_inquiry.encode('utf-8')).hexdigest()).lower()
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data_request = dict(
                partner_id=self.credentials['partner_id'],
                ref_no=trx_id,
                item_code=item_code,
                timestamp=TIME_STAMP,
                signature=signature_inquiry,
            )
            url = self.endpoint['payment']
            client = httpx.Client()
            try:
                r = client.post(url, headers=headers, data=data_request)
                r.raise_for_status()
                if r.status_code == 200:
                    result = r.json()
                    return result
            except httpx.HTTPError as exc:
                return f'Error : {exc}'
            finally:
                client.close()

    # ========= RAZER =========== #

    def razer_voucher_check_stock(self, *args):
        if self.code == 'razer_voucher':
            product_code = args[0]
            array_credentials = [product_code, self.credentials['partner_id'], self.credentials['msg']]
            join_credentials = ''.join(array_credentials)
            pwd = (hashlib.sha1(join_credentials.encode('utf-8')).hexdigest())
            headers = {'Content-Type': 'text/xml'}
            data_request = "<?xml version='1.0' encoding='utf-8'?>"\
                "<ayopay><function>Stock Check</function>"\
                "<id>{}</id><pwd>{}</pwd>"\
                "<productcode>{}</productcode></ayopay>".format(self.credentials['partner_id'], pwd, product_code)
            url = self.endpoint['req_voucher']
            client = httpx.Client()
            try:
                r = client.post(url, headers=headers, data=data_request)
                xml_data = xmltodict.parse(r.text)
                result = json.dumps(xml_data['ayopay'])
                return result
            except httpx.HTTPError as exc:
                return f'Error : {exc}'
            finally:
                client.close()

    def razer_voucher_request(self, *args):
        if self.code == 'razer_voucher':
            prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            product_code = args[0]
            trx_id = prefix + '_' + product_code
            array_credentials = [trx_id, self.credentials['partner_id'], self.credentials['secret_token']]
            join_credentials = ''.join(array_credentials)
            pwd = (hashlib.sha1(join_credentials.encode('utf-8')).hexdigest())
            headers = {'Content-Type': 'text/xml'}
            data_request = "<?xml version='1.0' encoding='utf-8'?>"\
                "<ayopay><function>Request XML</function>"\
                "<id>{}</id><trx>{}</trx><pwd>{}</pwd>"\
                "<productcode>{}</productcode>"\
                "</ayopay>".format(self.credentials['partner_id'], trx_id, pwd, product_code)
            url = self.endpoint['req_voucher']
            client = httpx.Client()
            try:
                r = client.post(url, headers=headers, data=data_request)
                xml_data = xmltodict.parse(r.text)
                result = json.dumps(xml_data['ayopay'])
                return result
            except httpx.HTTPError as exc:
                return f'Error : {exc}'
            finally:
                client.close()
