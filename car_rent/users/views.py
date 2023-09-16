from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .forms import RegistrationForm, LoginForm, ProfileForm
from .models import UserProfile
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


def show_user(request, user_slug):
    print(f"Requested user_slug: {user_slug}")
    user_profile = get_object_or_404(UserProfile, slug=user_slug)
    context = {
        'user_profile': user_profile,
        'title': f"{user_slug}"
    }
    return render(request, 'users/profile.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('users:login')
