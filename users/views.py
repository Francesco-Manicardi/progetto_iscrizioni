from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "user_create.html"
    success_url = reverse_lazy("home")


class UserUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "user_edit.html"
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy("centri_list")

    def get_object(self, queryset=None):
        return self.request.user
