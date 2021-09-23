import os
from pathlib import Path

CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

BASE_DIR = Path(__file__).resolve().parent.parent

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'tinymce',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'circle.apps.core',
    'circle.apps.partner',
    'circle.apps.store',
    'circle.apps.promo',
    'circle.apps.cart',
    'circle.apps.order',
    'circle.apps.payment',
    'circle.apps.account',
    'circle.apps.news',
    'circle.apps.api',
    'django_celery_beat',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'circle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'circle.apps.store.context_processors.menu_categories',
                'csp.context_processors.nonce'
            ],
        },
    },
]

WSGI_APPLICATION = 'circle.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "800px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10
}


# AUTH_USER_MODEL = 'account.AccountUser'
LOGIN_REDIRECT_URL = '/account/dashboard/'
LOGIN_URL = '/account/login/'

# ========= API Config ============ #
API_V1_PREFIX = 'api/v1/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}

# CONTENT SECURITY POLICY

CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = [
    "'self'",
    "'unsafe-inline'",
    "https://stackpath.bootstrapcdn.com",
    "https://cdn.jsdelivr.net",
    "https://code.jquery.com",
    "https://unpkg.com",
]
CSP_STYLE_SRC = ["'self'",
                 "'unsafe-inline'",
                 "https://cdn.jsdelivr.net",
                 "https://fonts.googleapis.com",
                 "https://unpkg.com",
                 "https://stackpath.bootstrapcdn.com"]
CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com", "data:"]
CSP_IMG_SRC = ["'self'",
               "http://www.w3.org",
               "https://*.yodu.id",
               "https://yodu.id", "https://wp.com", "https://*.wp.com",
               "www.google-analytics.com", "data:"]
CSP_INCLUDE_NONCE_IN = ['script-src']
CSP_CONNECT_SRC = ("'self'",
                   "www.google-analytics.com")
CSP_OBJECT_SRC = ["'self'"]
CSP_BASE_URI = ["'self'"]
CSP_FRAME_ANCESTORS = ["'self'"]
CSP_FORM_ACTION = ["'self'"]
CSP_MANIFEST_SRC = ["'self'"]
CSP_WORKER_SRC = ["'self'"]

# ========= Third Party Config =========== #


# === WORD PRESS === #
WP_ENDPOINT = 'http://berita.yodu.id/wp-json/wp/v2/'
