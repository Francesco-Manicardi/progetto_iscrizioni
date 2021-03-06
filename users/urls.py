from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name="register"),
    path('user_edit', login_required(views.UserUpdateView.as_view()), name="user_edit"),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(next_page=reverse_lazy("login")), name="logout"),
]
