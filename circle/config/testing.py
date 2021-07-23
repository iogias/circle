import os

from .base import *  # noqa : F403

DEBUG = True

SECRET_KEY = '1Ni-T0LonG*dI24h@5i4KAn_YA!'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),  # noqa
    }
}
