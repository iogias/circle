from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from circle.apps.account.api import views as user_api
from circle.apps.news import api as news_api

app_name = 'api'

router = routers.DefaultRouter()


urlpatterns = [
    # path(settings.API_V1_PREFIX + '/', views.NewsView.as_view(), name='check'),
    #     path('', include(router.urls)),
    #     path('auth/', CreateAccessView.as_view(), name='auth'),
    #     path('refreshtoken/', RefreshAccessView.as_view(), name='refresh_access'),
    path('news_list/', news_api.AllNewsView.as_view(), name='newslist'),
    path('news_categories_list/', news_api.NewsCategoriesView.as_view(),
         name='news_categories_list'),
    path('news_by_category/<int:cat_id>/page/<int:num_page>',
         news_api.NewsByCategoryView.as_view(), name='news_by_category'),
    path('user/<str:wallet_id>',
         user_api.UserApiView.as_view(), name='user_by_wallet_id'),
    path('user/profile/<str:wallet_id>',
         user_api.UserProfileApiView.as_view(), name='user_profile_by_wallet_id'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
