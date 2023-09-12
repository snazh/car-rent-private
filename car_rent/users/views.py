from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm
from .utils import DataMixin


class SignUp(DataMixin, CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('register')
    template_name = 'users/registration.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title="Registration")
        return {**context, **title}

    class Meta:
        pass

