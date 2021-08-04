import datetime

import pytest
from django.urls import reverse
from django.utils import timezone


def test_promo_str(promo_fixture):
    assert promo_fixture.__str__() == 'Promo Hari Ini'


def test_promo_reverse(client, promo_fixture):
    promo = promo_fixture
    url = reverse('promo:promo_detail', args=[promo.id, promo.slug])
    response = client.get(url)
    assert response.status_code == 200


def test_get_ongoing_promo(promo_fixture):
    promo_ended = promo_fixture.ended
    now = timezone.now()
    ongoing_promo = now - datetime.timedelta(days=1) <= promo_ended <= now
    assert ongoing_promo is True
