from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_experiences, name='all_experiences'),
    path('experience/<int:experience_id>/', views.view_experience_details, name='experience_details'),
]
