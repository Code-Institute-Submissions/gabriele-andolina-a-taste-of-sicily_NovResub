from django.contrib import admin
from .models import Category, Food, Pairing


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


class PairingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Pairing, PairingAdmin)
