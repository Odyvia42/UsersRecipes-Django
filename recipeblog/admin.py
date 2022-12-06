from django.contrib import admin

# Register your models here.

from .models import User, Recipe

# admin.site.register(User)
admin.site.register(Recipe)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'registration_date', 'status']
