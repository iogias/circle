from django.conf import settings
from django.urls import path

from circle.apps.api import views

app_name = 'api'

urlpatterns = [
    path(settings.API_V1_PREFIX + 'news/', views.get_all_latest_news, name='newslist'),
]
