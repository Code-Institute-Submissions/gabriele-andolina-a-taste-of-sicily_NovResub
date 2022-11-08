from django.contrib import admin
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'price',
    )

    ordering = ('name',)


admin.site.register(Experience, ExperienceAdmin)
