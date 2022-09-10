from django.contrib import admin
from .models import Category, Wine, Food, ExperienceType

# Register your models here.
admin.site.register(Category)
admin.site.register(Wine)
admin.site.register(Food)
admin.site.register(ExperienceType)