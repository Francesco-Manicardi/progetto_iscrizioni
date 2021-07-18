from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name="register"),
    path('user_edit', views.UserUpdateView.as_view(), name="user_edit"),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]
