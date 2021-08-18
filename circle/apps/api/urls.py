from django.conf import settings
from django.urls import path

from circle.apps.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    # path(settings.API_V1_PREFIX + '/', views.NewsView.as_view(), name='check'),
    path(settings.API_V1_PREFIX + 'news/', views.AllNewsView.as_view(), name='newslist'),
    path(settings.API_V1_PREFIX + 'api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
