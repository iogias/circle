from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from circle.apps.api import views

app_name = 'api'

urlpatterns = [
    # path(settings.API_V1_PREFIX + '/', views.NewsView.as_view(), name='check'),
    path('news_list/', views.AllNewsView.as_view(), name='newslist'),
    path('news_categories_list/', views.NewsCategoriesView.as_view(), name='news_categories_list'),
    path('news_by_category/<int:cat_id>/page/<int:num_page>',
         views.NewsByCategoryView.as_view(), name='news_by_category'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
