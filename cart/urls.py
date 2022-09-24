from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:wine_id>/', views.add_wine, name='add_wine'),
    path('add/<int:food_id>/', views.add_food, name='add_food'),
    path('adjust/<int:wine_id>/', views.adjust_wine_quantity,
         name='adjust_wine_qty'),
    path('adjust/<int:food_id>/', views.adjust_food_quantity,
         name='adjust_food_qty'),
    path('remove/<int:wine_id>/', views.remove_wine, name='remove_wine'),
    path('remove/<int:food_id>/', views.remove_food, name='remove_food'),
]
