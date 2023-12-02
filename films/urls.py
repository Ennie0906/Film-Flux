
from django.urls import path
from .views import views

urlpatterns = [
    path('films/', views.films_view, name='films'),
]
