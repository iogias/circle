from django.urls import path

from . import views

app_name = 'promo'

urlpatterns = [
    path('', views.promo_list, name='promo_list'),
    path('<int:id>/<slug:slug>/', views.promo_detail, name='promo_detail')
]
