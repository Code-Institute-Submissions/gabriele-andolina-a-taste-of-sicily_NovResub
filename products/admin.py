from django.contrib import admin
from .models import Category, Wine, Food, ExperienceType


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )


class WineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'vintage',
        'price',
        'image',
    )

    ordering = ('name',)

    prepopulated_fields = {"slug": ("name",)}


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'price',
        'image',
    )

    ordering = ('name',)

    prepopulated_fields = {"slug": ("name",)}


class ExperienceTypeAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'duration',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(ExperienceType, ExperienceTypeAdmin)
