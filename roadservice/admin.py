from django.contrib import admin
from .models import User
from . import models
# Register your models here.

admin.site.site_header = "OnRoadService System admin"
admin.site.index_title = "Admin"


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'mobile', ]


@admin.register(models.CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):
    list_display = ['customerService', 'carName',
                    'phoneNumber', 'location', 'address', 'message']


@admin.register(models.CarEngineers)
class CarEngineersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone_number', 'garage_location', 'email']
