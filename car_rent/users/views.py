from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm
from .utils import DataMixin


class SignUp(DataMixin, CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('cars:home')
    template_name = 'users/registration.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title="Registration")
        return {**context, **title}


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title="Login")
        return {**context, **title}

    def get_success_url(self):
        return reverse_lazy('cars:home')


def logout_user(request):
    logout(request)
    return redirect('users:login')
