from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Add other fields as needed

    def clean_username(self):  # custom validator
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError('Too short username')
        elif len(username) > 30:
            raise ValidationError('Too long username')
        return username


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()
