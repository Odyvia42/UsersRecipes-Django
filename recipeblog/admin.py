from django.contrib import admin

# Register your models here.

from .models import User, Recipe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'registration_date', 'status']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'dish_type', 'author', 'publication_date', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
