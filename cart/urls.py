from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:food_id>/', views.add_food, name='add_food'),
    path('adjust/<int:food_id>/', views.adjust_food_quantity,
         name='adjust_food_qty'),
    path('remove/<int:food_id>/', views.remove_food, name='remove_food'),
]
