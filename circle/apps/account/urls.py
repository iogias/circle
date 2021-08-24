from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'account'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='account/login.html', form_class=LoginForm),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.account_register, name='register'),

]
