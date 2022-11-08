from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_experiences, name='all_experiences'),
]