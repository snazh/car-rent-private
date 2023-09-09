from django.db import models


# Create your models here.

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
    properties = models.ForeignKey('CarProperty', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post about car'
        verbose_name_plural = 'Posts about cars'
        ordering = ['-created_at', 'title']


class CarProperty(models.Model):
    model = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, verbose_name='URL', db_index=True, max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    features = models.TextField(blank=False)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = 'Car properties'
        ordering = ['model', 'year']


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    additional_contact_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RentalDeal(models.Model):
    car = models.ForeignKey('CarProperty', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')],
                              default='active')

    def __str__(self):
        return f"Deal ID: {self.pk} - {self.car} ({self.start_date} to {self.end_date})"
