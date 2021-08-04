import pytest
from pytest_factoryboy import register

from tests.factories import PromoFactory

register(PromoFactory)


@pytest.fixture()
def promo_fixture(db, promo_factory):
    promo = promo_factory.create()
    return promo
