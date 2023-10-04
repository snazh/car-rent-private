from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'slug', 'daily_rent_cost', 'created_at', 'updated_at', 'is_published']
    list_filter = ['status', 'created_at', 'updated_at', 'is_published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'photo', 'slug', 'year', 'price']
    list_editable = ['photo']
    list_filter = ['vendor', 'year']
    search_fields = ['model', 'vendor']
    prepopulated_fields = {'slug': ('model',)}


@admin.register(RentalDeal)
class RentalDealAdmin(admin.ModelAdmin):
    list_display = ['car', 'client', 'start_date', 'end_date', 'total_cost', 'status']
    list_filter = ['status', 'start_date', 'end_date']
    search_fields = ['car__model', 'client__first_name', 'client__last_name']


@admin.register(Search)
class RentalDealAdmin(admin.ModelAdmin):
    list_display = ['name', 'lng', 'lat', 'date', 'active']
    list_editable = ['lng', 'lat', 'active']
