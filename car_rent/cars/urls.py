from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *
app_name = 'cars'
urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
]
