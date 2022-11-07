from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='all_products'),
    path('food/<int:food_id>/', views.view_food_details, name='food_details'),
    path('add/', views.add_food_to_store, name='add_food_to_store'),
    path('edit/<int:food_id>/', views.edit_food_in_store, name='edit_food_in_store'),
    path('delete/<int:food_id>/', views.delete_food_from_store, name='delete_food_from_store'),
]
