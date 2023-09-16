from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, verbose_name='URL', db_index=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:user_profile', kwargs={'user_slug': self.slug})
