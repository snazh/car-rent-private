from django.urls import path, include
from .views import *

app_name = 'users'
urlpatterns = [

    path('register/', SignUp.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('user_profile/<slug:user_slug>/', show_user, name='user_profile'),

    # Add other URLs as needed
]
