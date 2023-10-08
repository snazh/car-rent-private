from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'cars'
urlpatterns = [
    path('', index, name='home'),
    path('car-posts', CarView.as_view(), name='cars'),
    path('car-details/<slug:car_slug>/', CarDetails.as_view(), name='car_details'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('map/', MapView.as_view(), name='map'),
    path('add-car/', AddCarView.as_view(), name='add_car'),
    path('success/', successful_post, name='success')

]
# path('', cache_page(80)(HomeView.as_view()), name='home'),
# path('about/', cache_page(80)(about), name='about'),
