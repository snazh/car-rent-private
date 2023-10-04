from django.db import models
import datetime
from django.urls import reverse
from users.models import UserProfile


# Create your models here.


def user_avatar_upload_to(instance, filename):
    # Assuming you have a UserProfile model with a OneToOneField to the User model
    car_slug = instance.slug
    current_time = datetime.datetime.now()
    filename = f'{current_time}_{filename}'
    return f'cars/{car_slug}/{filename}'


class Car(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, verbose_name='URL', db_index=True, max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to=user_avatar_upload_to, null=True, blank=True)
    features = models.TextField(blank=False)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['model', 'year']


class CarCategory(models.Model):
    name = models.CharField(max_length=255,
                            choices=[('economy', 'Economy'), ('standard', 'Standard'), ('luxury', 'Luxury')],
                            default='economy')

    def __str__(self):
        return self.name


class CarPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, verbose_name='URL', db_index=True, max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('rented', 'Rented'),
                                                      ('under_repair', 'Under Repair')], default='available')
    daily_rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='time of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='time of update')
    is_published = models.BooleanField(default=True)
    properties = models.ForeignKey(Car, on_delete=models.CASCADE)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post about car'
        verbose_name_plural = 'Posts about cars'
        ordering = ['-created_at', 'title']


class RentalDeal(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')],
                              default='active')

    def __str__(self):
        return f"Deal ID: {self.pk} - {self.car} ({self.start_date} to {self.end_date})"


class Search(models.Model):
    name = models.CharField(max_length=60, verbose_name='Branch name')
    lng = models.FloatField(verbose_name='Longitude')
    lat = models.FloatField(verbose_name='Latitude')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.name
