from django.contrib import admin
from user.models import User
from rental.models import Car


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_admin']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_year']
    list_display_links = ['name', 'create_year']
