from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:wine_id>/', views.add_wine, name='add_wine'),
    path('add/<int:food_id>/', views.add_food, name='add_food'),
]
