from django.contrib import admin
from .models import Category, Food


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
