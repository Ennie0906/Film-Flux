
from django.urls import path
from .views import (Films)

urlpatterns = [
    path('films/', views.films_view, name='films'),
]
