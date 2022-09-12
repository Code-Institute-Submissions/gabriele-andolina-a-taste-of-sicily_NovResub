from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='all_products'),
    path('wine/<int:wine_id>/', views.view_wine_details, name='wine_details'),
    path('food/<int:food_id>/', views.view_food_details, name='food_details'),
]
