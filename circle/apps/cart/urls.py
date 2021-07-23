from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('q/inquiry_item/', views.inquiry_item, name='inquiry_item')
]
