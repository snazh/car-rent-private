
from django.urls import path, include
from .views import *
app_name = 'users'
urlpatterns = [

    path('register/', SignUp.as_view(), name='register'),

    # Add other URLs as needed
]