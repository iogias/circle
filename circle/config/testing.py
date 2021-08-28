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


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')  # noqa : F403
TINYMCE_JS_URL = STATIC_URL + 'tinymce/tinymce.min.js'
